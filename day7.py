#Day 7 of learning python --string operatiosn 
#string is a combination of characters including abc..123..!@#...  (spaces too)
'''strings are immutable in python, cannot change actual string value, 
   can perform just operations and funtion.
'''
#string concatination
str1="chetan"
str2="sreeja"
print(str1+" "+str2)

#length of string
str3="yashu"
print(len(str3))

#string indexing (starts from 0----) (counts spaces and special characters)
str4="chetan"
print(str4[5])
print(str4[6]) #Indexerror: index out of bouce  
str4[0]="h"
print(str4) #TypeError: 'str' object does not support item assignment

#string slicing --->accesing parts of string
country="india"
print(country[0:4]) #returns "indi" as output
print(country[0:len(country)]) #returns from 0 to length of string-->Till end of index
print(country[:4]) #starts from zero(python automatically takes)
print(country[2:]) #python automatically takes len[country]
print(country[1]) #returns only index value [1]

#--Negative indexing
print(country[-3:-1]) #returns "pl"  

#String functions (the real string value doesnot changes)
college="pbr visvodaya"
college.endswith("ya") #checks if string ends with "ya"-->returns True/False
college.capitalize() #caplitalize first letter of string
college.replace("pbr","abr") #replaces letters or words in string and displays
college.find("pbr") #finds whether the word is there or not ?? returns index value if present
college.count("pbr") #counts how many time the word is occured

#program to take input of a string and find its length
n=input("enter input:")
print(f'''length of string "{n}" is {len(n)}''')

#program to find $ in a string
i="Hey my daily payout in america is 99.9$"
i.find("$")
