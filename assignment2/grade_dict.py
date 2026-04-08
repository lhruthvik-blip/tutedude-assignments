#!/usr/bin/python3


# 2 Student Grades
#Create a dictionary where the keys are student names and the values are their grades. 
#Allow the user to:
#Add a new student and grade.
#Update an existing student’s grade.
#Print all student grades.

student_grades = {}
while True:
    action = input("input from the list for action as specified : 1 or add, 2 or update, 3 or print, or 4 or quit: ")
    
    if action == "1" or action == "add":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        student_grades[name] = grade
        print(f"Added {name} with grade {grade}.")
        
    elif action == "2" or action == "update":
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} not found.")
            
    elif action == "3" or action == "print":
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
            
    elif action == "4" or action == "quit":
        break
        
    else:
        print("Invalid action. Please choose add, update, print, or quit.")