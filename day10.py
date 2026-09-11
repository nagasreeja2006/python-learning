#day 10 of python learning --Sets
'''
  Set is the collection of the unordered items.
  Each element in the set must be unique & immutable.
  sets in Python do not allow index-based access. They are:
  Unordered → elements dont have a fixed position.
  Unindexed → you cant do set2[0] like you would with a list or tuple.
  Unique → duplicates are automatically removed.
'''
set1={1, 2, 3, 4}
print(set1)
print(len(set1)) #prints length of set
set2={1, 2, 2, 2}
print(set2) #returns only {1, 2} --> duplicate elements not allowed
print(set2[0]) #type error , indexing not allowed in sets
newSet=set() #creates empty set
newSet={} #not allowed to create empty set, it creates empty dictionary

#===== Sets methods =====
subjects = {"Python", "SQL"}
subjects.add("JAVA") #add element in set
subjects.update(["ML", "GenAI", "Git"]) #add multiple elements at once
subjects.remove("Python")#remove element in set
subjects.pop() #removes a random value in set
subjects.clear() #empties the set
print(subjects)


#operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b)) #a is intersected to b
print(a|b) # union(|) prints everything in both sets
print(a-b) #elements in (a) but not in (b)
print(b-a) #elements in (b) but not in (a)

#loops + sets
subjects = {"Python", "SQL", "ML", "GenAI"}
for subject in subjects:
    print(subject)

""" programs """ 

#list of numbers, remove all duplicate numbers.
list1=[10, 20, 10, 30, 20, 40, 30]
set1=set(list1) #converts list to set
print(set1)

#Find elements that are present in both lists.
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
set1=set(list1)
set2=set(list2)
print(set1.intersection(set2))

#Unique Subjects
subjects = [
    "Python",
    "SQL",
    "Python",
    "ML",
    "SQL",
    "GenAI",
    "Python"
]
unique_subjects = set(subjects)
print(unique_subjects)

#student manage
morning = {"Chetan", "Ravi", "Rahul", "Arun"}
evening = {"Rahul", "Arun", "Kiran", "Sreeja"}
print(morning & evening) #prints who are in both groups-->intersection(&)
print(morning - evening) #prints students in morning not in evening
print(evening - morning) #prints students in evening not in morning
print(morning | evening) #prints all students in both sets
