#day 9 of python learning tuples
'''
Tuple is a built in datatype that lets us create "immutable" sequence of values
'''
tuple=(2,1,3,1)
print(type(tuple))
print(tuple[0]) # print index 0 value
print(tuple[1]) #print index 1 value
#tuple[0]=5 # not accepted in python because tuple is inmmutable 
print(tuple[1:3]) #prints (1,3)

#tuple methods--->
print(tuple.index(1)) #returns index of value of given element of its first occcurance
print(tuple.count(1)) #counts and return , how many times the element occured

#for storing a single element in tuple
tup=(1) #error
tup=(1,) #correct way

'''example programs'''
#to count the number of students with the “A” grade in the following tuple
tup = ["C", "D", "A", "A", "B", "B", "A"]
print(tup.count("A"))

#Store the above values in a list & sort them from "A" to "D"
tup = ["C", "D", "A", "A", "B", "B", "A"]
tup.sort()
print(tup)

#Create a tuple containing 5 numbers and print: First number,Last number,Length of tuple
tup = (10, 20, 30, 40, 50)
print("First number:", tup[0])# Print the first number
print("Last number:", tup[-1])# Print the last number
print("Length of tuple:", len(tup)) # Print the length of the tuple

#Using a loop, print every element.
tup=("Python", "Java", "C++", "JavaScript", "SQL")
for i in tup:
  print(i)

#Create a tuple of 10 numbers: print only even
tup=(1,2,3,4,5,6,8,9,10)
for num in tup:
    if num % 2 == 0:
        print(num)

        
# Create a tuple of movie names and Ask the user for a movie name and Check if the movie exists in the tuple
movies = ("Inception", "Interstellar", "Avatar", "Titanic", "The Matrix")
movie_name = input("Enter a movie name: ")
if movie_name in movies:
    print(f"Yes, {movie_name} is in the list!")
else:
    print(f"Sorry, {movie_name} is not in the list.")

#prints student details whose marks is greater than 80
students = (
    ("Chetan", 85),
    ("Rahul", 72),
    ("Sreeja", 91),
    ("Yashu", 68)
)
for name, marks in students: #unpacking tuple
    if marks >= 80:
        print(name, marks)


#Create a tuple containing numbers and print sum
numbers = (10, 20, 30, 40, 50) 
sum=0
for i in numbers:
  sum=sum+i
print(sum)
