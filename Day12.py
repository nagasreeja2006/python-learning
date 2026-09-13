#day 12 of learning python --->List comprehension
#List comprehension is a short way to create a new list from an existing sequence.
"""
   syntax--->
   list=[
    #data Transformation
    #for loop
    #data filtering (optional)
   ]
"""
#--->before list comprehension
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)

#--->after list comprehension
squares=[i*i for i in range(1,6)]
print(squares)

#Create squares of numbers from 1 to 10.
squares=[i*i for i in range(1,11)]
print(squares)

#Even Numbers
even=[i for i in range(1,11) if i%2==0]
print(even)

#Filtering Marks only above 50
marks = [35, 78, 45, 90, 22, 67, 30, 88]
new_marks=[mark for mark in marks if mark>=50]
print(new_marks)

#Create a list containing the cubes of numbers from 1 to 10.
lis=[i**3 for i in range(11)]
print(lis)

#odd numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers=[i for i in numbers if i%2!=0]
print(new_numbers)

#Create a list containing only marks greater than or equal to 60.
marks=[25, 45, 67, 89, 32, 90, 55, 41]
new_marks=[mark for mark in marks if mark>=60]
print(new_marks)

#Create a new list containing the length of each name.
names = ["chetan", "ram", "sita", "arjun"]
len_names=[len(name) for name in names]
print(len_names)

#Create a list containing the squares of only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_square=[num*num for num in numbers if num%2==0]
print(even_square)

#create a list containing J letter
names=["John","James","Emmy","Michael","Jimmy"]
new_names=[name for name in names if "J" in name]
new_names


#create a list , delete www. and lower all the characters and filter non website names
domains=["www.google.com","www.Facebook.com","localhost","www.OPEnai.com"]
clean=[d.lower().replace("www.","") for d in domains if "." in d]
print(clean)

#using list comprhension cub of number 1 to 10 who are even
cube=[x ** 3 for x in range(11) if x%2==0]
print(cube)
