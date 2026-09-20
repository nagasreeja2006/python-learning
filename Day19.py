#day 19 of python learning --- Lambda Function
# A lambda function is a small anonymous function.

#before lambda
def even(x):
    if x%2==0:
        return "its is even"
    else:
        return "its is odd"
x=int(input("Enter a number: "))
print(even(x))    

#lamda if else syntax
#lambda arguments: expression if condition else expression
#using lambda function
even_num=lambda x: "its is even" if x%2==0 else "its is odd"
print(even_num(int(input("Enter a number: "))))

#Lambda with Two Parameters
add=lambda x,y: x+y
print(add(10,20))

#Lambda with Multiple Parameters
multiply=lambda x,y,z: x*y*z
print(multiply(2,3,4))

#Lambda with Conditional Expression
check=lambda age=10: "Adult" if age>=18 else "Minor"
print(check())

#examples Create a lambda function to add two numbers.

add_two=lambda a,b: a+b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Addition of {a} and {b} is {add_two(a,b)}")

#Create a lambda function to find the square of a number.
square=lambda x: x*x
num=int(input("Enter a number: "))  
print(f"Square of {num} is {square(num)}")

#Create a lambda function to check whether a person is eligible to vote.
is_eligible=lambda age: True if age >= 18 else False
age=int(input("Enter your age: "))
print(f"Is the person eligible to vote? {is_eligible(age)}")

#Create a lambda function to find the greater number between two numbers.
greater=lambda a,b: a if a>b else b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"The greater number between {a} and {b} is {greater(a,b)}")

#Create a lambda function that checks whether a student's marks result in:
# "Pass" or "Fail" based on a passing mark of 40.
result=lambda marks: "Pass" if marks>=40 else "Fail"
marks=int(input("Enter marks: "))
print(f"The student has {result(marks)} the exam.")

#5 lambda functions:
add = lambda a, b: a + b
square = lambda n: n * n
even_odd = lambda num: "even" if num % 2 == 0 else "odd"
pass_fail = lambda marks: "pass" if marks >= 35 else "fail"
greater = lambda A, B: A if A > B else B

while True:
    print("\n1. Addition\n2. Square\n3. Even/Odd\n4. Pass/Fail\n5. Greater Number\n6. Exit")
    choice = input("Enter your choice : ")

    if choice == "1":
        a = int(input("Enter number a : "))
        b = int(input("Enter number b : "))
        print(f"{a} + {b} = {add(a, b)}")

    elif choice == "2":
        n = int(input("Enter a number : "))
        print(f"Square of {n} = {square(n)}")

    elif choice == "3":
        num = int(input("Enter a number : "))
        print(f"{num} is {even_odd(num)}")

    elif choice == "4":
        marks = int(input("Enter marks : "))
        print(f"Result: {pass_fail(marks)}")

    elif choice == "5":
        A = int(input("Enter first number : "))
        B = int(input("Enter second number : "))
        print(f"Greater number is {greater(A, B)}")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
