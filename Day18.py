#day 18 of learning python --- *args and **kwargs
# *args allows a function to accept any number of positional arguments.

#before
def add(a, b):
    return a + b  #only 2 arguments can be passed

#after
def add(*args):
    return sum(args)  #can accept any number of arguments
result = add(10, 20, 30, 40)
print(result)  #100

#printing the arguments passed to the function
def show_numbers(*numbers):
    print(numbers)
show_numbers(10,20,30,40)

#loop
def show(*numbers):
    for number in numbers:
        print(number)

show(10, 20, 30)

#perform calculations
sum=0
def add(*numbers):
  global sum
  for num in numbers:
    sum=sum+num
  return sum

result=add(10,20,30)
print(result)

"""----**kwargs----"""
# **kwargs allows a function to accept any number of keyword arguments.
#it stores the arguments in a dictionary
def student(**details):
    print(details)

student(
    name="Chetan",
    age=20,
    branch="AIML"
)

#wrong way to use **kwargs
'''
student(
    "name"="Chetan",  #error, keyword arguments should be in key=value format
    "age"=20,
    "branch"="AIML"
)
'''

#function to print key-value pairs
def profile(**pro):
  for key,items in pro.items():
    print(key,":",items)
    
print(profile(name="chetan",age=19,branch="AIML")) 

#example programs

#1.Add Multiple Numbers (*args)
def add_numbers(*args):
   total=0
   for num in args:
      total=total+num
   return total
print(add_numbers(10,20,30,40,50))   

#2.Student Result System (*args + **kwargs)
def student_result(*marks, **details):
  print("details")
  for key,value in details.items():
    print(key,":",value)

  print("----marks----")
  total=0
  for i in marks:
    total=total+i
  print("total:",total)  
  average=total/len(marks)
  print("average:",average)
result=student_result(10,20,30,name="chetan",age=19,branch="AIML")    
print(result) 

#3.Find Maximum Number (*args)
def find_maximum(*args):
  maximum=args[0]
  for num in args:
    if num>maximum:
      maximum=num
  return maximum
result=find_maximum(10,20,30,40,50)
print(result)

#Example 4 — Employee Information (**kwargs)
def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

result=employee_info(name="Chetan", age=25, department="AIML", salary=50000)
print(result)

#Example 5 — Calculate Average (*args)
def calculate_average(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    average = total / len(numbers)
    return average

result = calculate_average(10, 20, 30, 40, 50)
print("Average =", result)


#1st assignment Shopping Cart 🛒

def calculate_total(*prices):
  total=0
  for i in prices:
    total=total+i
    average=total/len(prices)
  print("total:",total)
  print("average:",average)
  
print(calculate_total(10,20,30,40,50))  



#Assignment 2 — Student Management Function

def student_management(*marks, **details):
  total = 0
  print("=== Student Details ===")
  for key, value in details.items():
    print(key, ":", value)
  print("=== Marks ===")
  for mark in marks:
    print(mark)
    total = total + mark
  average = total / len(marks)
  print("Total:", total)
  print("Average:", average)
student_management(
    90, 85, 78, 95,
    name="Chetan",
    age=19,
    branch="AIML"
)


def data(**info):
  for key,value in info.items():
    print(key,":",value)

data(name="chetan",age=19,branch="AIML")
