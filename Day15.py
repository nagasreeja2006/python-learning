#day 15 of learning python --- Functions

#A function is a reusable block of code that performs a specific task.


#without function

print("Hello, World!")
print("Hello, World!")
print("Hello, World!")  #typing the same code again and again is not efficient


#with function

def hi():
    print("Hello, World!")

hi()  #calling the function
hi()  #can use the function multiple times without rewriting the code


#basic function with variable

hm = "chetan"

def hi():
    print(hm)

hi()


#another basic function

def welcome():
    print("Welcome to Python")

welcome()


#basic student information function

def student_info():
    print("Name: Chetan")
    print("Age: 20")
    print("Branch: AIML")

student_info()


#basic greeting function

def greet():
    print("Hello! Have a good day")

greet()


#using function multiple times

def line():
    print("===================")

line()
print("Python Learning")
line()
print("Day 15")
line()


#simple practice function

def python():
    print("I am learning Python Functions")

python()


#basic function practice

def morning():
    print("Good Morning Chetan")
morning()
morning()

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



#mini example program using loops with functions
#Assignment 1: Greeting Function and print three times details
def greet(name):
    print(name)
    print("Welcome to Python programming 😊")

for i in range(3):
    greet("chetan")

# Assignment 1: Multiplication Table 
def multiplication_table(number, n=10):
    for i in range(1,n+1):
      print(number,"x",i,"=",number*i)
      
multiplication_table(5)  
print("=========")
multiplication_table(6,n=10)

# Assignment 2 — Student Profile
def student_profile(name, branch="AIML", year=3):
  print("Name:",name)
  print("Branch:",branch)
  print("year:",year)

student_profile("chetan")
print("====")
student_profile("kiran","CSE")
print("====")
student_profile("kishore","ECE",1)



# Assignment 3 — Simple Interest Calculator
# Formula: Simple Interest = (principal × rate × time) / 100

def simple_interest(principal, rate=5, time=1):
    return (principal * rate * time) / 100

# Example calls
print("Simple Interest =", simple_interest(1000))              # uses default rate=5, time=1
print("Simple Interest =", simple_interest(2000, rate=10))     # custom rate
print("Simple Interest =", simple_interest(1500, rate=7, time=3))  # custom rate & time
