#day 22 of python learning --- File Handling
#File -- A file is a named location on disk to store related information. 
# It is used to permanently store data in a non-volatile memory (e.g. hard disk, SSD, etc.).

#without storing in file 
a=[1,2,3,4,5]
a.append(6)
print(a) # when program ends, the data is lost

#Why do we need file handling?
"""
    Save user data
    Read saved data
    Store application information
    Create reports
    Maintain logs
    Store expenses
    Store student records
"""
#Types of files
""" 
    Text files # can be open in notepad, wordpad, etc.
     i.txt
     ii.csv
     iii.json
     iv.html
     v.py
    Binary files # can be open in image viewers, media players, etc., if open shows(dcshvhcua#@fvhs..binary data)
     .jpg
     .png
     .mp3
     .mp4
     .pdf
      .exe
"""
#python has built-in functions for creating, writing, and reading files.
#1.open() function
#syntax: open(filename, mode)
f = open("demofile.txt", "r")   #"r" - Read - Default value. Opens a file for reading, error if the file does not exist
f = open("demofile.txt", "a")   #"a" - Append - Opens a file for appending, creates the file if it does not exist
f = open("demofile.txt", "w")   #"w" - Write - Opens a file for writing, creates the file if it does not exist

#MODE 1 — r (READ)
file = open("notes.txt", "r") #read existing file
#file not found ->shows error
data = file.read()
print(data)
file.close() #close the file after reading

#MODE 2 — w (WRITE)
file = open("notes.txt", "w") #create or overwrite existing file
data=file.write("Hello, World!") #if file already has data, it will overwrite the existing content
print(data) #prints number of characters written to the file
file.close() #close the file after writing

#MODE 3 — a (APPEND)
file = open("notes.txt", "a") #create or append to existing file
data = file.write("Appended text!") #appends text to the end of the file
print(data) #prints number of characters written to the file
file.close() #close the file after appending

#MODE 4 — x (CREATE)
file = open("newfile.txt", "x") #create a new file, if file already exists, it will show error
file.close() #close the file after creating


#using with statement to open a file --> no need to close the file, it will automatically close the file after the block of code is executed

#READING FILES 
#1.read() method
with open("notes.txt","r") as file:
    data=file.read() #reads the entire file
    print(data)

#2.readline() method
with open("notes.txt","r") as file:
    data=file.readline() #reads the first line of the file
    print(data)
    #continue reading the next line
    data=file.readline() #reads the second line of the file
    print(data)

#3.readlines() method
with open("notes.txt","r") as file:
    data=file.readlines() #reads all the lines of the file and returns a list of lines
    print(data) #prints list of lines

#4.read(number)
with open("notes.txt","r") as file:
    data=file.read(5) #reads first 5 characters of the file
    print(data)
    #continue reading the next 5 characters
    data=file.read(5) #reads next 5 characters of the file
    print(data)


#WHY \n APPEARS? 
# due to the way files are read, the newline character (\n) is included in the string when reading lines from a file. When you use the readlines() method, it reads each line of the file and includes the newline character at the end of each line. This is why you see \n in the output when printing the lines read from a file.

#to remove unecessary spaces , use strip() method
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())


#FILE CURSOR
# The file cursor is a pointer that keeps track of the current position in the file. When you open a file, the cursor is initially positioned at the beginning of the file. As you read or write data to the file, the cursor moves forward accordingly. You can also manually move the cursor to a specific position in the file using methods like seek().
with open("notes.txt", "r") as file:
    print(file.read(6)) #reads first 6 characters of the file
    print(file.read(5)) #reads next 5 characters of the file

#tell()
# The tell() method returns the current position of the file cursor in the file. It tells you the number of bytes from the beginning of the file to the current cursor position.
with open("notes.txt", "r") as file:
    print(file.read(6)) #reads first 6 characters of the file
    print(file.tell()) #prints the current position of the cursor in the file
    print(file.read(5)) #reads next 5 characters of the file
    print(file.tell()) #prints the current position of the cursor in the file

#seek()
# The seek() method is used to move the file cursor to a specific position in the file. It allows you to reposition the cursor to a desired location, enabling you to read or write data from that point onward.
with open("notes.txt", "r") as file:
    print(file.read(6)) #reads first 6 characters of the file
    print(file.tell()) #prints the current position of the cursor in the file
    file.seek(0) #moves the cursor to the beginning of the file
    print(file.read(5)) #reads first 5 characters of the file
    print(file.tell()) #prints the current position of the cursor in the file


#WRITING FILES

#write() method
# The write() method is used to write a string to a file.
# It returns the number of characters written to the file.

with open("notes.txt", "w") as file:
    data = file.write("Hello Chetan")
    print(data) #prints number of characters written


#WRITING MULTIPLE LINES
# We can use multiple write() methods to write multiple lines to a file.
# \n is used to move the text to a new line.

with open("students.txt", "w") as file:
    file.write("Chetan\n")
    file.write("Ravi\n")
    file.write("Manasa\n")


#WRITELINES() METHOD
# The writelines() method is used to write multiple strings to a file at once.
# It accepts a list of strings.

students = [
    "Chetan\n",
    "Ravi\n",
    "Manasa\n"
]

with open("students.txt", "w") as file:
    file.writelines(students)


#IMPORTANT
# writelines() does not automatically add a new line (\n).
# We need to add \n manually if we want each item on a new line.

languages = [
    "Python",
    "Java",
    "C++"
]

with open("languages.txt", "w") as file:
    file.writelines(languages)

#output in file will be:
#PythonJavaC++


#correct way to write each item on a new line

languages = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open("languages.txt", "w") as file:
    file.writelines(languages)


#READING FILE USING FOR LOOP
# We can directly loop through a file.
# Each iteration reads one line from the file.

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())


#MODE r+ (READ AND WRITE)
# The r+ mode allows us to read and write to a file.
# The file must already exist.
# It does not delete the existing content.

with open("notes.txt", "r+") as file:
    data = file.read()
    print(data)

    file.write("\nNew line added")


#MODE w+ (WRITE AND READ)
# The w+ mode allows us to write and read from a file.
# It creates the file if it does not exist.
# If the file already exists, it deletes all existing content.

with open("notes.txt", "w+") as file:
    file.write("Hello Chetan")

    #after writing, cursor is at the end of the file
    #so we use seek(0) to move the cursor to the beginning

    file.seek(0)

    data = file.read()
    print(data)


#MODE a+ (APPEND AND READ)
# The a+ mode allows us to append and read from a file.
# It creates the file if it does not exist.
# It does not delete the existing content.
# New data is always added to the end of the file.

with open("notes.txt", "a+") as file:
    file.write("\nNew note added")

    #move cursor to beginning to read the complete file

    file.seek(0)

    data = file.read()
    print(data)


#COMPLETE FILE MODES SUMMARY

"""
r  - Read. File must exist.
w  - Write. Creates file if it does not exist and overwrites existing content.
a  - Append. Creates file if it does not exist and adds data to the end.
x  - Create. Creates a new file and gives an error if the file already exists.

r+ - Read and Write. File must exist.
w+ - Write and Read. Creates file if missing and overwrites existing content.
a+ - Append and Read. Creates file if missing and adds data to the end.
"""


#TEXT MODE
# By default, Python opens files in text mode.
# "r" is the same as "rt".

with open("notes.txt", "rt") as file:
    data = file.read()
    print(data)


#BINARY MODE
# Binary mode is used for files like images, videos, audio, PDF files, etc.
# "b" represents binary mode.

# rb - Read Binary
# wb - Write Binary
# ab - Append Binary

#Example:

#with open("image.jpg", "rb") as file:
#    data = file.read()


#FILE ENCODING
# Encoding tells Python how to read and write characters in a text file.
# UTF-8 is the most commonly used encoding.
# It supports English, Telugu, Hindi, emojis and many other characters.

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("నేను Python నేర్చుకుంటున్నాను 🔥")


#FILE PATHS
# A file path tells Python where the file is located.

#1.Relative Path
# When the file is in the same folder as the Python program.

#open("notes.txt", "r")


#2.File inside another folder

#Example project structure:

"""
MyProject/
│
├── main.py
├── notes.txt
│
└── data/
    └── students.txt
"""

#To open students.txt:

#open("data/students.txt", "r")


#3.Absolute Path
# Complete location of the file in the computer.

#Example Windows path:

#C:\\Users\\Chetan\\Documents\\notes.txt

#open("C:\\Users\\Chetan\\Documents\\notes.txt", "r")


#COMMON FILE ERRORS

#1.FileNotFoundError
# Happens when we try to open a file in read mode but the file does not exist.

#open("missing.txt", "r")


#2.PermissionError
# Happens when Python does not have permission to access the file.


#3.UnsupportedOperation
# Happens when we try to perform an operation that is not allowed in the current file mode.

#Example:

#with open("notes.txt", "r") as file:
#    file.write("Hello")


#DAY 22 FILE HANDLING SUMMARY

"""
open()       - Opens a file

r            - Read
w            - Write
a            - Append
x            - Create

read()       - Reads complete file
read(n)      - Reads specific number of characters
readline()   - Reads one line
readlines()  - Reads all lines as a list

write()      - Writes data to a file
writelines() - Writes multiple strings to a file

tell()       - Returns current cursor position
seek()       - Moves cursor to a specific position

r+           - Read and Write
w+           - Write and Read
a+           - Append and Read

rt           - Read text
rb           - Read binary

with open()  - Automatically closes the file
"""                              



#Personal Details File
name = input("Enter your name: ")
age = input("Enter your age: ")
branch = input("Enter your branch: ")
college = input("Enter your college: ")

with open("details.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Branch: " + branch + "\n")
    file.write("College: " + college + "\n")

print("Details saved successfully!")


#Read Personal Details
with open("details.txt", "r") as file:
    data = file.read()
    print("\nYour Details:")
    print(data)


#Student Name Saver using (A)
name = input("Enter student name: ")

with open("students.txt", "a") as file:
    file.write(name + "\n")
print("Student added successfully!")


#View All Students
with open("students.txt", "r") as file:
    for stu in file:
        print(stu.strip())

#Count Students
with open("students.txt", "r") as file:
    students = file.readlines()
    print("Total number of students:", len(students))   

#Search for a Student 🔍      
search_name = input("Enter student name to search: ")
found = False
with open("students.txt", "r") as file:
    for student in file:
        if student.strip().lower() == search_name.lower():
            found = True
            break
if found:
    print("Student found!")
else:
    print("Student not found!")   


#Clear a File
with open("students.txt", "w") as file:
    file.write("") #writing empty string to clear the file

#Mini Project: Student Record Manager
while True:

    print("\n--- STUDENT RECORD MANAGER ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Count Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")

        with open("students.txt", "a") as file:
            file.write(name + "\n")

        print("Student added successfully!")

    elif choice == "2":

        with open("students.txt", "r") as file:

            print("\n--- STUDENT LIST ---")

            for student in file:
                print(student.strip())

    elif choice == "3":

        search_name = input("Enter student name to search: ")

        found = False

        with open("students.txt", "r") as file:

            for student in file:

                if student.strip().lower() == search_name.lower():
                    found = True
                    break

        if found:
            print("Student found!")
        else:
            print("Student not found!")

    elif choice == "4":

        with open("students.txt", "r") as file:
            students = file.readlines()

        print("Total students:", len(students))

    elif choice == "5":

        print("Exiting program...")
        break

    else:

        print("Invalid choice!")



#Simple Notes Manager
#FUNCTION TO ADD NOTES

def add_notes():
    with open("notes.txt", "a") as file:
        note = input("Enter your note: ")
        file.write(f"{note}\n")
    print("Note added successfully!")


#FUNCTION TO VIEW NOTES

def view_notes():
    with open("notes.txt", "r") as file:
        notes = file.readlines()
        if len(notes) == 0:
            print("No notes available!")
        else:
            print("\n--- YOUR NOTES ---")
            for note in notes:
                print(note.strip())

#FUNCTION TO COUNT NOTES
def count_notes():
    with open("notes.txt", "r") as file:
        notes = file.readlines()
        print("Total Notes:", len(notes))

#FUNCTION TO CLEAR NOTES
def clear_notes():
    with open("notes.txt", "w") as file:
        file.write("")
    print("All notes cleared successfully!")

#MAIN PROGRAM
while True:
    print("\n--- NOTES MANAGER ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Count Notes")
    print("4. Clear Notes")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_notes()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        count_notes()
    elif choice == "4":
        clear_notes()
    elif choice == "5":
        print("Exiting Notes Manager...")
        break
    else:

        print("Invalid choice! Please try again.")
