#day 13 of learning python----Nested Datastructures
""" Nested = one data structure inside another data structure. """

"""=======Nested Lists======"""
#normal list-->
#names = ["Chetan", "Sreeja", "Yashu"]
#nested List-->
names=[
    ["chetan",20],
    ["sreeja",21],
    ["yashu",18]
]
"""
              0             1
         ┌────────┐     ┌─────┐
index 0  │ Chetan │     │ 20  │
         └────────┘     └─────┘

             0             1
index 1  │ Sreeja │     │ 21  │

             0             1
index 2  │ Yashu  │     │ 20  │

"""
print(names) #prints list
print(names[0]) # prints "chetan",20
print(names[1]) #prints "sreeja",21
print(names[0][1]) #prints chetan age
print(names[1][1]) #prints sreeja age
print(names[2][1]) #prints yashu age


#accesing nested list in line by line
for name in names:
    print(name[0],name[1]) # name[0]=chetan,...  name[1]=20,....

#nested list + nested loops
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    for num in row:
      print(num)

#print like matrix
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    for num in row:
      print(num,end=" ")
    print()


"""====Nested Dictionaries===="""

student = {
    "name": "Chetan",
    "details": {
        "age": 20,
        "branch": "AIML"
    }
}

print(student["name"]) #display student name
student.get("name") #another method to display student name
print(student["details"]["branch"]) #display branch name in details
print(student["details"]["age"]) #display age in details


"""==List inside dictionary=="""
student = {
    "name": "Chetan",
    "skills": ["Python", "SQL", "ML"]
}
print(student["skills"]) #prints skills
print(student["skills"][0]) #prints index 0 in skills  ->python
print(student["skills"][1]) #prints index 1 in skills  ->Sql
print(student["skills"][2]) #prints index 2 in skills  ->ML
print(student["name"],student["skills"]) #prints name and skills
#Loop through skills:
for skill in student["skills"]:
   print(skill)   #prints skills one by one
#Loop through skills and name :
for name,skill in student.items():
   print(name,":",skill)   #prints skills and name one by one   




"""====dictionary inside list===="""
students = [
    {
        "name": "Chetan",       #index 0
        "age": 20
    },
    {
        "name": "Sreeja",       #index 1
        "age": 21
    },
    {
        "name": "Yashu",       #index 2
        "age": 20
    }
]

print(students[0]["name"]) #print chetan index 0
print(students[1]["age"]) #print sreeja age index 1
print(students[2]["name"]) #print yashu index 2
#Loop Through List of Dictionaries
for s in students:
   print(s["name"]) #print all names in dictionaries accross list
for i in students:
   print(i["age"]) #print all ages in dictionaries accross list



"""----Loop Through List of Dictionaries----"""
students = [
    {
        "name": "Chetan",
        "age": 20,
        "branch": "AIML"
    },
    {
        "name": "Sreeja",
        "age": 21,
        "branch": "CSE"
    },
    {
        "name": "Yashu",
        "age": 20,
        "branch": "ECE"
    }
]

for student in students:
    print(student["name"])  #print(names of all studnets) 
for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Branch:", student["branch"])
    print()




'''---Nested Dictionary + List---'''
students = {
    "student1": {
        "name": "Chetan",
        "skills": ["Python", "SQL", "ML"]
    },
    "student2": {
        "name": "Sreeja",
        "skills": ["Java", "SQL"]
    }
}

print(students["student1"])
print(students["student1"]) #prints student 1 details
print(students["student1"]["skills"]) #prints student 1 skills
print(students["student2"]["skills"][0]) #prints student 2 skills index 0
for name,skills in students["student1"].items():
    print(name,":",skills)   #prints student1 details


#example programs---real life gadget shop
products = [
    {
        "name": "Laptop",
        "price": 60000,
        "brands": ["HP", "Dell", "Lenovo"]
    },
    {
        "name": "Phone",
        "price": 25000,
        "brands": ["Samsung", "OnePlus", "Poco"]
    }
]
#print product names
for product in products:
  print(product["name"])
#print prices  
for product in products:
  print(product["name"],":",product["price"])

#print brands
for product in products:
  print(product["name"]) 
  for brand in product["brands"]:
    print("-",brand)


#nested datastructures +  if
students = [
    {"name": "Chetan", "marks": 85},
    {"name": "Sreeja", "marks": 92},
    {"name": "Yashu", "marks": 65}
]

for student in students:

    if student["marks"] >= 80:
        print(student["name"], "Excellent")

    elif student["marks"] >= 60:
        print(student["name"], "Good")

    else:
        print(student["name"], "Needs Improvement")    


#nested data 
data = {
    "students": [
        {
            "name": "Chetan",
            "skills": ["Python", "SQL"]
        },
        {
            "name": "Sreeja",
            "skills": ["Java", "HTML"]
        }
    ]
}
print(data["students"][0]["skills"][0])  #students-->0 index--->"skills"-->index 0



#print matrix
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
for num in numbers:
  for n in num:
    print(n,end=" ")
  print()

#print student details who got above 80
students = [
    {"name": "Chetan", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Sreeja", "marks": 91},
    {"name": "Yashu", "marks": 68},
    {"name": "Ananya", "marks": 77}
]
for student in students:
  if student["marks"]>90:
    print(student)


#print skills
student = {
    "name": "Chetan",
    "skills": ["Python", "SQL", "Git", "ML"]
}
for s in student["skills"]:
  print(s)

#ask max price from user and print available items or products
products = [
    {
        "name": "Laptop",
        "price": 55000,
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 3200,
        "category": "Footwear"
    },
    {
        "name": "Coffee Maker",
        "price": 4500,
        "category": "Home Appliances"
    },
    {
        "name": "Smartphone",
        "price": 28000,
        "category": "Electronics"
    },
    {
        "name": "Backpack",
        "price": 1200,
        "category": "Accessories"
    }
]
price=int(input("enter max price u can afford:"))
for p in products:
  if p["price"]<=price:
    print("Product Name:",p["name"],"| Price:",p["price"],"| Category:",p["category"])
