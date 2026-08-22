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
fact = 5
i = 1
while i <= 5:
    fact *= i 
    i += 1
print("Factorial:", fact)

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
