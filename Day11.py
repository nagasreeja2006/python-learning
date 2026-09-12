#day 11 of python learning -->Dictionaries
"""
  Dictionaries are used to store data values in key:value pairs
  They are unordered, mutable(changeable) & dont allow duplicate keys
  Basic Syntax-->
      dictionary = {
    key: value,
    key: value
}
"""
#creating a dictionary
student = {
    "name": "Chetan", #key=name and value=chetan
    "age": 20,
    "marks":{
        "Maths":90,
        "Physics":100,
        "Chemistry":99
    }
}
print(student["name"]) #returns values of names(key) in dictionary
print(student.get("name")) #another way of getting output of key
""" why use get() ?
- `student["branch"]` → ❌ KeyError if `"branch"` doesnt exist.  
- `student.get("branch")` → ✅ returns `None` instead of error.  
- `student.get("branch", "Not Available")` → ✅ returns `"Not Available"` if key is missing.  

👉 **Use `get()` when a key might not exist, to avoid errors and provide a safe default.**
"""
print(student["age"]) #returns values of age(key) in dictionary
print(student["marks"]["Physics"]) #retuns 100, go to marks and sub element physics=100
student["age"]=21 #if age key exists change value of age in existing dictionary
"""
 create new value syntax -->
 dictionary["new_key"] = value
"""
student["branch"]="AIML" #if new key ,adds new key (branch) and value (AIML) to dictionarydictionary["new_key"] = value
print(student)


my_dict = {
    "name": "Rahul", #key=name and value=chetan
    "age": 20,
    "city":"Nellore",
    "Gender":"Male",
    "Caste":"OC"
}
my_dict.pop("age") #removes age key totally from dictionary
del my_dict["city"] #another way to remove key totally from dictionary
print(my_dict.keys()) #prints all keys in dictionary
print(my_dict.values()) #prints all values in dictionary
print(my_dict.items()) #prints all dictionary like --->(key,value)

#using a loop printing all keys and values and items in dictionary
my_dict1={
    "name":"yashu",
    "age":18
}
for i in my_dict1.keys():
    print(i)
for j in my_dict1.values():
    print(j)    
for key,value in my_dict1.items():
    print(key,":",value)    
   

#set methos===>update()
#used to update an dictionary
College={
    "Name":"Pbr visvodaya",
    "Location":"Kavali"
}
print(College)
College.update({
    "Category":"Engineering College"
}) 
'''update can also add update such as keys in dictionary and can also change existing values in dictionary
update()
   ↓
Add new keys
   +
Update existing keys
'''
print(College)


"""
        ==Dictionaries cheat sheet==
            keys()       → all keys
            values()     → all values
            items()      → key + value
            get()        → safely get a value
            update()     → add/update items
            pop()        → remove an item
            keys   → WHAT ARE THE KEYS?
            values → WHAT ARE THE VALUES?
            items  → GIVE ME BOTH
            get    → GIVE ME THIS VALUE
            update → ADD/CHANGE DATA
            pop    → REMOVE DATA
"""
