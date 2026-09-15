# day 14 of python learning ---> mini project program

"""===== Student Management System ====="""
student = [

    {
        "name": "Chetan",
        "age": 19,
        "branch": "AIML",
        "marks": 99,
        "skills": ["Python", "MongoDB", "Django"]
    }

]
while True:
  print("===student management system===")
  print("1. Add Student")
  print("2. View Students")
  print("3. Search Student")
  print("4. Show Students Above 80")
  print("5. Show Highest Marks")
  print("6. Show Unique Branches")
  print("7. Exit")
  choice=input("Enter Your Choice:")
  if choice=="1":
    print("==ADDING A STUDENT==")
    student_name=input("Enter Student name:")
    student_age=int(input("Enter Student age:"))
    student_branch=input("Enter Student Branch:").upper()
    student_marks=int(input("Enter Student marks:"))
    skill_1=input("Enter Skill 1:")
    skill_2=input("Enter Skill 2:")
    skill_3=input("Enter Skill 3:")
    student_dict={
      "name":student_name,
      "age":student_age,
      "branch":student_branch,
      "marks":student_marks,
      "skills":[
        skill_1,
        skill_2,
        skill_3
      ]
    }
    student.append(student_dict)
    print("Student added succesfully")

  elif choice=="2":
    if not student:
      print("NO Students to View !")
    else:
      print("====Student List:====")
      for s in student:
        print("name:",s["name"])
        print("age:",s["age"])
        print("branch:",s["branch"])
        print("marks:",s["marks"])
        print("Skills:")
        for skill in s["skills"]:
          print("-",skill)
        print("-----------")  
        
  elif choice=="3":
    if not student:
      print("No Students ")
    else:
      search=input("enter an student name to search:")
      found=False
      for s in student:
        if search.lower() in s["name"].lower():
          print("Students Found->")
          print("name:",s["name"])
          print("age:",s["age"])
          print("branch:",s["branch"])
          print("marks:",s["marks"])
          print("skills:")
          for skill in s["skills"]:
            print("-",skill)
          print("--------")  
          found=True
      if found==False:        
        print("Student Not Found!")
    
  elif choice=="4":
    if not student:
      print("No students found now to sort")
    else:
      print("Students Above or equal to 80 marks:")
      found=False
      for s in student:
        if s["marks"]>=80:
          print("name",s["name"])
          print("age:",s["age"])
          print("branch:",s["branch"])
          print("marks:",s["marks"])
          print("skills:")
          for skill in s["skills"]:
            print("-",skill)
          found=True
          print("------")
      if found==False:
        print("No students have scored above 80 marks !")

  elif choice=="5":
    if not student:
      print("No students available")
    else:
      highest=student[0]
      for s in student:
        if s["marks"]>highest["marks"]:
          highest=s
      print("TOP PERFORMER:")
      print("name",highest["name"])
      print("age:",highest["age"])
      print("branch:",highest["branch"])
      print("marks:",highest["marks"])
      print("skills:")
      for skill in highest["skills"]:
        print("-",skill)
      print("--------")

  elif choice=="6":
    if not student:
      print("No Students available !")
    else:
      print("Unique Branches:")
      branch=set()
      for s in student:
        branch.add(s["branch"])
      #now display branch one by one  
      for b in branch:
        print("-",b)
          
  elif choice=="7":
    print("Thank You !")
    break

  else:
    print("Invalid input")
