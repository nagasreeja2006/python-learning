#day 16 of learning python --- Parameters and Return
'''
global variable = A variable that is defined outside of any function 
and can be accessed from any part of the code, including inside functions.
'''
#function with parameter

def greet(name):
    print("Hello", name)

greet("Chetan")
greet("Manasa")


#function with two parameters

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Chetan", 20)


#function with multiple parameters

def student_info(name, branch, age):
    print("Name:", name)
    print("Branch:", branch)
    print("Age:", age)

student_info("Chetan", "AIML", 20)


#function with return value
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
#can directly print function return value
print(add(5, 10))


#function with parameter and return value
def square(a):
    return a * a
print(square(5))
result = square(10)
print(result)


#addition function
def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(10, 20)
print(result)


#even or odd function
def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = check(10)
print(result)


#largest number function
def largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return f"{num1} is the largest number"
    elif num2 >= num1 and num2 >= num3:
        return f"{num2} is the largest number"
    else:
        return f"{num3} is the largest number"
result = largest(10, 20, 30)
print(result)


#factorial function
def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
factorial = fact(5)
print(f"The factorial of 5 is: {factorial}")


#calculate area of circle
def area_of_circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area
area = area_of_circle(5)
print(f"The area of the circle with radius 5 is: {area}")


"""===Example programs==="""

"""====Calculator program using functions===="""
def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b
  
while True:
  print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
  choice=input("Enter Your Choice :")
  if choice == "1":
    print("==Addition==")
    a=int(input("input (a) value:"))
    b=int(input("input (b) value:"))
    result=add(a,b)
    print(f"Addition of {a} and {b} is {result}")

  elif choice == "2":
    print("==Subtraction==")
    a=int(input("input (a) value:"))
    b=int(input("input (b) value:"))
    result=sub(a,b)
    print(f"Subtraction of {a} and {b} is {result}")

  elif choice == "3":
    print("==Multiplication==")
    a=int(input("input (a) value:"))
    b=int(input("input (b) value:"))
    result=mul(a,b)
    print(f"Multiplication of {a} and {b} is {result}")

  elif choice == "4":
    print("==Division==")
    a=int(input("input (a) value:"))
    b=int(input("input (b) value:"))
    if b == 0:
      print("Error ! cant divide by Zero")
    else:
      result=div(a,b)
      print(f"Division of {a} and {b} is {result}")
      
  elif choice == "5":
    print("Execution Closed !")
    break

  else:
    print("Select only given options !")



#global variable = A variable that is defined outside of any function and can be accessed from any part of the code, including inside functions.
"""===ATM program using functions==="""    
AccountBalance = 5000

def checkBalance():
  return AccountBalance

def deposit(amount):
  global AccountBalance
  if amount < 0:
    return "Invalid Deposit !"
  else:
    AccountBalance=amount+AccountBalance
    return AccountBalance
    
def withdraw(amount):
  global AccountBalance
  if amount > AccountBalance:
    return "Insufficient Balance"
  else:
    AccountBalance = AccountBalance - amount
    return AccountBalance
print("====Chetan Banking System====")
while True:
  print("1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
  choice = input("Enter Your Choice : ")
  if choice == "1":
    print("===========")
    print("Your Available balance =",checkBalance())
    print("===========")

  elif choice == "2":
    print("===========")
    amount=int(input("Enter amount to deposit = "))
    result=deposit(amount)
    if result == "Invalid Deposit !":
      print("Invalid Deposit !, amount should be more than zero(0)")
    else:
      print("--DEPOSIT SUCCESSFULL--")
      print(f"Your Updated Balance = ",AccountBalance)
    print("===========")

  elif choice == "3":
    print("===========")
    amount=int(input("Enter amount to withdraw = "))
    result=withdraw(amount)
    if result == "Insufficient Balance":
      print(f"Insufficient Balance | your Current balance is {AccountBalance}")
    else:
      print("--WITHDRAW SUCCESSFULL--")
      print(f"Balance Left = {AccountBalance}")
    print("===========")  

  elif choice == "4":
    print("Thanks For Using Banking System ! bye..🙌")
    break

  else:
    print("===========")
    print("Select Valid Option !")
    print("===========")
