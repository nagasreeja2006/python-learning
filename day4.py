# Day 4 of learning python if-else, if-elif-else, nestedif 
'''If else (checks a condition and executes a block of code if the condition is true,
otherwise executes another block of code)'''
username = input("Enter username: ")
password = input("Enter password: ")

if username == "chetan" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

#If elif else
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 50:
    print("C Grade")
else:
    print("Fail")

#Nested if
age = int(input("Enter your age: "))

if age >= 18 and age <= 100:
    citizen = input("Are you a citizen of india ? yes/no: ")

    if citizen == "yes":
        print("Eligible to vote")
    elif (citizen == "no"):
        print("Not eligible because citizenship is required")    
    else:
        print("choose yes or no")

else:
    print("You are under 18")

#example 2 marks grading system
n=int(input("enter a number:"))
if n>0:
    if n%2==0:
        print("even number and positive number")
elif n<0:
    print("negative number")
elif n==0:
    print("zero")
else:
    print("invalid input")
