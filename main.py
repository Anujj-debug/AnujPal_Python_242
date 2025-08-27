print("helllo")

#camel case
myVariableName = "hello"
#snake case
my_variable_name = "hello"
#pascal case
MyVariableName = "hello"

z = (str)(123)
print(z)
print(type(z))

#one value to multiple variables (it has same id)
a = b = c = 10
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))

#many values to multiple variables (it has different id)
x , y , z = "Orange" , "Banana" , "Cherry"
print(id(x))
print(id(y))
print(id(z))

#Unpacking a collection
fruits = ["apple" , "banana" , "cherry"]
x , y , z = fruits
print(x)
print(y)
print(z)

#Global variable
x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc()    

def myfunc2():
    global g
    g = "fantastic"

myfunc2()

print("Python is " + g)
