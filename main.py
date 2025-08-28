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

#Datatypes
var1 = 1
var2 = True
var3 = 10.023
var4 = 10 + 3j

print(id(var1))
print(id(var2))
print(id(var3))
print(id(var4))

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

#string datatypes
print("hello")
print('Hello')
#Multiline string
a = """Lorem feffdfdfdffef,
ffdfdfefefeffffwfwfwfwff,
wfefwwfefwefefefefwff"""
print(a)

print(len(a))
print(a[4])

#check string
txt = "The best things in life are free!"
print("free" in txt)

text = "The best things in life are freee!"
print("best" not in text)

#Slicing String
b = "Hello,World"
print(b[2:5])  #end is exclusive
print(b[:3])
print(b[-5:-2]) #end is inclusive and start is exclusive

#Modify strings
a = "    Hello , World!    "
print(a.upper())
print(a.lower())
print(a.strip()) #removes the extra whitespaces