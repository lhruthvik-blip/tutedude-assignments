const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const axios = require('axios');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

// Serve form
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'form.html'));
});

// Handle form submission
app.post('/submit', async (req, res) => {
  try {
    const response = await axios.post('http://backend:5000/process', req.body, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });
    if (response.data.success) {
      res.redirect('/success');
    } else {
      res.send(`Error: ${response.data.error}`);
    }
  } catch (error) {
    console.error('Backend error:', error.message);
    console.error('Full error:', error);
    res.status(500).send('Error connecting to backend: ' + error.message);
  }
});

// Success page
app.get('/success', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'success.html'));
});

app.listen(3000, () => {
  console.log('Frontend running on port 3000');
});
