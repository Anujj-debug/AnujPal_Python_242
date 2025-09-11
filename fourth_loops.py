i = 0
while i<6 :
    i+=1
    if i == 3 :
        continue
    print(i)

fruits = ["apple" , "banana" , "cherry"]    
for x in fruits :
    print(x)
type(fruits)

for y in "apple" :
    print(y) 

#break
i = 0
while i<6 : 
    i+=1
    if i == 3 :
        break
    print(i) 

#range
for i in range(10) :
    print(i) 
for i in range(2,30, 3) :  #from 2 to 30 with step 3
    print(i)          

#while else
i =1 
while i<6 :
    print(i)
    i+=1
else :
    print("finally")   

#range else 
for i in range(6) :
    print(i)
else :
    print("finally")       

#nested loops
a = ["A" , "B" , "C"]
fruits = ["apple" , "banana" , "cherry"]
for x in a :
    for y in fruits :
        print(x , y)

for j in [0,1,2,3] :
    pass    