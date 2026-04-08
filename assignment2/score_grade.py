#1. Grade Checker
#Take a score as input and print the grade based on the following:
#90+ : "A"
#80-89 : "B"
#70-79 : "C"
#60-69 : "D"
#Below 60 : "F"
#here we used a basic if else statement to carry out marks and all.

score = int(input("Enter your score: "))
print("score", score )
if score >= 90:
    print("Grade: A")   
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")