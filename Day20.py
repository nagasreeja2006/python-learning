#day 20 of python learning --- map(), filter(), reduce()

#map() function applies a given function to all items in an iterable (like list, tuple etc.) and returns a map object (which is an iterator).
#syntax: map(function, iterable)
#map--to perform operation on every item of iterable


#Square Every Number
numbers = [1, 2, 3, 4, 5]
square=list(map(lambda x: x*x,numbers))
print(square)

#map() Without Lambda
def square_func(x):
    return x * x
square=list(map(square_func,numbers))
print(square)

##Convert Names to Uppercase
names=["chetan","kiran","sam"]
new_names=list(map(lambda x:x.upper(),names))
print(new_names)

#Add 10 to Every Number
numbers=[10,20,30,40,50]
new=list(map(lambda x:x+10,numbers))
print(new)

#Use map() and lambda to add 5 grace marks to every student.
marks = [35, 50, 67, 80, 90]
new_marks=list(map(lambda mark:mark+5,marks))
print(new_marks)

#use map() to use true or false for each number in a list based on whether it is even or odd.
numbers = [10, 15, 20, 25, 30]
new=list(map(lambda x:True if x%2==0 else False,numbers))
print(new)

#filter() is used to select only the items that satisfy a condition.
'''
   map()    → changes EVERY item

   filter() → selects SOME items
'''
#program to filter even numbers from a list using filter() and lambda function
#syntax---list(filter(lambda item: condition, data))

#no need to use if else statement in filter() function, it automatically filters the items based on the condition provided.
numbers = [10, 15, 20, 25, 30]
new =list(filter(lambda x:x %2==0,numbers))
print(list(new))

#Numbers Greater Than 50
numbers = [20, 55, 70, 10, 90, 45]
num=list(filter(lambda n:n>50,numbers))
print(num)

#Filter Passed Students
marks = [20, 35, 80, 25, 90, 30]
new=list(filter(lambda n:n>=35,marks))
print(new)




#reduce() --combines all items into one result
#reduce() -takes multiple values and repeatedly combines them until only one final value remains.
from functools import reduce #import reduce function from functools module
marks=[10,20,30,40]
new=reduce(lambda x,y:x+y,marks) #doesnot need an use of list()
print(new)

#largest number in a list
from functools import reduce
marks=[1,2,3]
new=reduce(lambda x,y:x if x>y else y,marks)
print(new)

"""
MAP
Many → Many
Change every item


FILTER
Many → Some
Keep matching items


REDUCE
Many → One
Combine everything

MAP

[1, 2, 3]
     ↓
[2, 4, 6]


FILTER

[1, 2, 3, 4]
     ↓
[2, 4]


REDUCE

[1, 2, 3, 4]
     ↓
10


syntax--->
# MAP
list(map(lambda x: operation, data))

# FILTER
list(filter(lambda x: condition, data))

# REDUCE
from functools import reduce

reduce(lambda x, y: operation, data)
"""
