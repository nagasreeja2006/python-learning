#day 8 of learning python ---->Lists
'''
    "List is a built-in data type that stores set of values"
    "It can store elements of different types (integer, float, string, etc.)"
    "It can store multiple datatypes together
'''

#basic example
marks = [87, 64, 33, 95, 76] #create list
print(marks) #print list
print(type(marks)) #print datatype--> <class list >
marks[0]=99 #allowed in python (used to change index values in original list)
print(marks) 

#length of list
student=["karan",90,"Rahul"]
print(len(student)) #len(list) -> returns of length
student[0] #returns "karan"

#========"list slicing (similar to string slicing )======"
'''
    List_name[ starting_idx : ending_idx ] #ending idx is not included
    marks = [87, 64, 33, 95, 76]
    marks[ 1 : 4 ] is [64, 33, 95]
    marks[  : 4 ] is same as marks[ 0 : 4]
    marks[ 1 :  ] is same as marks[ 1 : len(marks) ]
    marks[ -3 : -1 ] is [33, 95]
'''

#========"list methods"========

list1=[2, 1, 3]
list1.append(4)  #adds one element at the end [2, 1, 3, 4]
list1.sort( )  #sorts in ascending order [1, 2, 3]
list1.sort( reverse=True )  #sorts in descending order [3, 1, 2]
list1.reverse( )  #reverses list 
list1.insert(0,9)  #insert element at index (list1.insert( idx, el ))
print(list1)

list2 = [2, 1, 3, 1]
list2.remove(1)  #removes first occurrence of element [2,3,1]
list2.pop(2)  #removes element at idx 


#======list + if else======
#Example: Check whether a number exists
list3=[10,20,30,40,50]
if 20 in list3:
    print("20 is present")
else:
    print("20 is not present")   

#Check list length
fruits = ["apple", "banana", "mango"]
if len(fruits) > 3:
    print("More than 3 fruits")
else:
    print("3 or less fruits")


#======List + for loop======
#Use a for loop to go through every item in a list.
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

#using if else check elements in list is even or odd
numbers = [10, 15, 20, 25, 30]
for number in numbers:
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")   

#======List + while loop=======
# print elements in list
fruits = ["apple", "banana", "mango"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1        

#List + While + If/Else
#prints numbers with displaying greater than 10 or lessthan or equal to 10
numbers = [5, 12, 7, 20, 15]
i = 0
while i < len(numbers):
    if numbers[i] > 10:
        print(numbers[i], "is greater than 10")
    else:
        print(numbers[i], "is less than or equal to 10")
    i += 1    


#=====program====
# to add user inputed 3 movie names in an empty list
movie1 = input("enter 1st movie : ")
movie2 = input("enter 2nd movie : ")
movie3 = input("enter 3rd movie : ")

lis = []
lis.append(movie1)
lis.append(movie2)
lis.append(movie3)
print(lis)


#To check if a list contains a palindrome of elements. (Hint: use copy( ) method)
lis1=list(input("enter a list:"))
copy_list1=lis1.copy()
copy_list1.reverse()
if (copy_list1==lis1):
    print("palindrome")
else:
    print("not a palindrome")
