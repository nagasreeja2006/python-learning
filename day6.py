#Day 6 of learning python "part-A"  break, continue, pass with while loop and for loop 
        #====================(i)while loop=================

'''
             === break statement ===
      break is used to stop the loop immediately.
'''
#print 1 to 10 numbers but stop at 6
i=1
while i<=10:
    if i==6:
        break
    print(i)
    i=i+1
#print 10 to 1  but stop at 6
i=10
while i>=1:
    if i==6:
        break
    print(i)
    i=i+1

'''
             === continue statement ===
      continue is used to skip the current iteration
'''    
#print 1 to 10 but skip 5
i=0
while i<=10:
    i=i+1 
    if i==5:
        continue #skip the current iteration 
    print(i)
#print 10 to 1 but skip 6    
i=10
while i>=1:
  i=i-1
  if i==6:
    continue #skip the current iteration 
  print(i) 

'''
             === pass statement ===
      pass is used as a null statement, it does nothing when executed
'''
i = 1

while i <= 5:
    if i == 3:
        pass # do nothing (usually saved for future code)
    print(i)
    i = i + 1

'''
            ====combination(pass,break,continue)======
'''    
#pass,break,continue
i = 0

while i < 10:

    i = i + 1

    if i == 3:
        pass

    elif i == 5:
        continue

    elif i == 8:
        break

    print(i)


#====================(ii)for loop=================

'''
             === break statement ===
      break is used to stop the loop immediately.
'''
#print 1 to 10 but stop at 6
for i in range(1,10):
   if i==6:
      break
   print(i)

#print 10 to 1 but stop at 7
for i in range(10,0,-1):
  if i==7:
    break
  print(i)

'''
             === continue statement ===
      continue is used to skip the current iteration only 1
''' 
#print 1 to 10 but skip 5
for i in range(1,11):
   if i==5:
      continue #skip iteration
   print(i)

#print 10 to 1 but skip 5
for i in range(10,0,-1):
   if i==5:
      continue #skip iteration
   print(i)   

'''
             === pass statement ===
      pass is used as a null statement, it does do nothing when executed
'''
for i in range(1, 6):

    if i == 3:
        pass
    #saved for future code purpose
    print(i)
'''
            ====combination(pass,break,continue)======
'''    
#break, continue and pass
for i in range(1, 11):

    if i == 3:
        pass

    elif i == 5:
        continue

    elif i == 8:
        break

    print(i)
