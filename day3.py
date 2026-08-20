#Day 3 of learning python operators

# arithmetci operators
a = 10
b = 3

print(a + b)   # Addition 13
print(a - b)   # Subtraction 7
print(a * b)   # Multiplication 30
print(a / b)   # Division 3.33
print(a % b)   # Modulus 1
print(a ** b)  # Power 1000
print(a // b)  # Floor Division

#comparison operators
c = 10
d = 20
print(c == d) # Output: False
print(c != d) # Output: True
print(c > d)  # Output: False
print(c < d)  # Output: True
print(c >= d) # Output: False
print(c <= d) # Output: True

#logical operators
#and
agee = 20
print(agee >= 18 and agee <= 25) # Output: True
#or
age = 30
print(age >= 18 or age <= 25) # Output: True
#not
chetan=True
sreeja=False 
print(not sreeja) 

#if else
a=int(input("enter a number:"))
if a==10:
    print("hello")
else:
    print("bye")

#if elif else
marks=int(input("enter marks:"))
if marks>=90:
    print("A grade")
elif marks>=80:
    print("B grade")    
elif marks>=70:
    print("C grade")    
else:
    print("fail")    


#login credentials
username="yashu"
password="yaswitha123"
user_input=input("enter username:")
password_input=input("enter password:")
if user_input==username and password_input==password:
    print("login successful")
else:
    print("login failed")    

#PROGRAM 1 — Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#PROGRAM 2 — Positive, Negative or Zero
number = float(input("Enter a number: "))
if number > 0:
    print("Positive number")

elif number < 0:
    print("Negative number")

else:
    print("The number is Zero")

#PROGRAM 3 — Largest of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(num1," is the largest number.")
elif num2 > num1:
    print(num2,"is the largest number.")   
else:
    print("Both numbers are equal.")
