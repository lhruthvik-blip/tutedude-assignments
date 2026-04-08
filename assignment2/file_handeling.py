#!/usr/bin/python3


#3.Write to a File
#Write a program to create a text file and write some content to it.
#Using file functions like write and open.
#4. Read from a File
#We used open in read mode and file.read to read and print to display.


# the script creates a file called sample.txt if it doesn't exist, and opens it in read/write mode. on each execution of the script, it reads the content of the file, prints it, and then appends a new line with the line number to the end of the file. Finally, it reads and prints the entire content of the file again before closing it.

from pathlib import Path

path = Path("sample.txt")
if path.exists():
    f=open('sample.txt','r+')
else:
    f=open('sample.txt','a+')


#print(f.readline()) # -> prints first line of the file
#print(f.readlines()) # -> prints the content of the file in list format
#print(l[1]) # -> prints the 2nd line of the file

print(f.read())
f.seek(0)
l=f.readlines()
len=len(l)+1
print("writing to a new line")
f.seek(0, 2) # -> moves the cursor to the end of the file
f.write("writing to line number {}".format(len) + "\n") # -> writes to the file at the end of the file
f.seek(0) # -> moves the cursor to the beginning of the file
print(f.read()) # > prints entire content of the file
f.close()