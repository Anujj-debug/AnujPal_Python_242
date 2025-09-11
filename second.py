#python takes input as string always
v = input("Enter your value ")
print(v)
print(type(v))
#to take integer input
v1 = int(input("enter your number : "))
print(v1)
print(type(v1))

#if else
a = 5
b = 3
print("A is greater") if a > b else print("B is greater")
if a > b : print("A is greater") 
else : print("B is greater")

a = 300
b = 300
print("A is greater") if a > b else print("Equal") if a == b else print("B is greater")

a = 200
b = 30
c = 500
if a > b and c > a :
    print("Both condition are true")


a = 33
b = 200
if not a > b :
    print("A is not greater than B")