#day 5 of learning python ( loops )

#while loop

#print numbers from 1 to 5 using while loop
i=1
while i<=5:
  print(i)
  i=i+1
print("end of loop")

#print 5 to 1 using while loop 
i=5
while i>=1: 
  print(i)
  i=i-1
print("end of loop")

#print numbers and hello from 1 to 10 using while loop
i=1
while i<=10:
  print("hello",i)
  i=i+1
print("end of loop")

# Ask user for a number
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i, end=" ")
    i = i + 1

#multiplication table using while loop
i=1
n=int(input("enter a number:"))
while i<=10:
  print(n,"X",i,"=",n*i)
  i=i+1
print("end of loop")

#sum of first 5 numbers using while loop
total=0
j = 1
while j <= 5:
    total=total+j
    j =j+ 1
print(total) 

#factorial of a number using while loop
n = int(input("Enter a number: "))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("Factorial =", fact)


# Print even and odd numbers separately
m=1
while m<=10:
  if m%2==0:
    print(m,"is even")
  else:
    print(m,"is odd")  
  m=m+1

#sum of even numbers from 1 to 10 using while loop
i=1
total=0
while i<=10:
  if i%2==0:
    total=total+i
  i=i+1
print(total)  

#sum of odd numbers from 1 to 10 using while loop
i=1
total=0
while i<=10:
  if i%2!=0:
    total=total+i
  i=i+1
print(total)  

#sum of first 10 even numbers
i=2
total=0
count=0
while count<10:
  total=total+i
  i=i+2
  count=count+1
print(total)

#sum of first 10 odd numbers
i=1
total=0
count=0
while count<10:
  total=total+i
  i=i+2
  count+=1
print(total)  



#For loop() and range() function

#---------range() function ---------
#range() function is used to generate a sequence of numbers. 
#It can take one, two, or three arguments.

range(6) # generates numbers from 0 to 5
range(1, 6) # generates numbers from 1 to 5
x=range(1, 11, 2) # generates numbers from 1 to 10 with a stepcount of 2

#---------for loop()---------
#for loop is used to iterate over a sequence 

#for loop to print 1 to 5
for i in range(6):
  print(i,end=" ")

#for loop to print 10 to 1 in reverse order
for i in range(10,0,-1):
  print(i,end=" ")
  
# for loop to print 5 to 20
for i in range(5,21):
  print(i,end=" ")  


#for loop to print even number from 1 to 10
for i in range(2,11,2):
  print(i,end=" ")


#for loop to print odd number from 1 to 10
for i in range(1,11,2):
  print(i,end=" ")

# Ask user for a number
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i, end=" ")

#for loop to print every character in a string
a="chetan"
for i in a:
  print(i)


#for loop to print multiplication table
n=int(input("enter a number:"))
for i in range(1,11):
  print(n,"x",i,"=",n*i)


#sum of numbers from 1 to 5 using for loop
sum=0
for i in range(1,6):
  sum=sum+i
print(sum)


#sum of  even numbers from 1 to 10 using for loop
sum=0
for i in range(2,11,2):
  sum=sum+i
print(sum)  


#sum of  odd numbers from 1 to 10 using for loop
sum=0
for i in range(1,11,2):
  sum=sum+i
print(sum)


#sum of first 10 even number using for loop
count=0
sum=0
for i in range(1,50):
  if i%2==0 and count<10:
    sum=sum+i
    count=count+1
print(sum) 


#sum of first 10 odd number using for loop
count=0
sum=0
for i in range(1,50):
  if i%2!=0 and count<10:
    sum=sum+i
    count=count+1
print(sum) 


#to find factorial of a number using for loop
fact=1
n=int(input("enter a number:"))
for i in range(1,n+1):
  fact=fact*i
print(fact)  


#==========example program ========
n=int(input("enter a input 1 or 2 :"))
if n==1:
  count=0
  sum=0
  for i in range(1,34):
   if i%2==0 and count<10:
      sum=sum+i
      count=count+1
  print("sum of first 10 even numbers:",sum)
elif n==2:
  count=0
  sum=0
  for i in range(1,34):
   if i%2!=0 and count<10:
      sum=sum+i
      count=count+1
  print("sum of first 10 odd numbers:",sum)
else:
  print("invalid invalid")
