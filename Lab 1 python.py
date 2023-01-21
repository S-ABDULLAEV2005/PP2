# PYTHON SYNTAX
#Exercise 1
print("Hello world")
#Exercise 2
if 5 > 2:
    print("Five is greater than two!")
#PYTHON COMMENT
#Exercise 1
#This is a comment
#Exercise 2
'''This is a comment
written in 
more that just one line'''
#PYTHON VARIABLES
#Exercise 1
carname = "Volvo"
#Exercise 2
x = 50
#Exercise 3
x = 5
y = 10
print(x + y)
#Exercise 4
x = 5
y = 10
z = x + y
print(z)
#Exercise 5
myfirst_name = "John"
#Exercise 6
x = y = z = "Orange"
#Exercise 7
def myfunc():
    global x
    x = "fantastic"
#PYTHON DATA TYPES
#Exercise 1
x = 5
print(type(x))
#int
#Exercise 2
x = "Hello World"
print(type(x))
#str
#Exercise 3
x = 20.5
print(type(x))
#float
#Exercise 4
x = ["apple", "banana", "cherry"]
print(type(x))
#list
#Exercise 5
x = ("apple", "banana", "cherry")
print(type(x))
#tuple
#Exercise 6
x = {"name" : "John", "age" : 36}
print(type(x))
#dict
#Exercise 7
x = True
print(type(x))
#bool
#PYTHON NUMBERS
#Exercise 1
x = 5
x = float(x)
#Exercise 2
x = 5.5
x = int(x)
#Exercise 3
x = 5
x = complex(x)
#PYTHON STRINGS
#Exercise 1
 x = "Hello World"
 print(len(x))
#Exercise 2 
txt = "Hello World"
x = txt[0]
#Exercise 3

txt = "Hello World"
x = txt[2:5]

#Exercise 4

txt = "Hello World"
x = txt.strip()

#Exercise 5
txt = "Hello World"
txt = txt.upper()
#Exercise 6
txt = "Hello World"
txt = txt.lower()
#Exercise 7
txt = "Hello World"
txt = txt.replace("H", "J") 
#Exercise 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#PYTHON BOOLEANS
#Exercise 1
print(10 > 9)
#True
#Exercise 2
print(10 == 9)
#Flase
#Exercise 3
print(10 < 9)
#False
#Exercise 4
print(bool("abc"))
#True
#Exercise 5
print(bool(0))
#False
#PYTHON OPERATORS
#Exercise 1
print(10 * 5)
#Exercise 2 
print(10 / 2)
#Exercise 3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
#Exercise 4
if 5 != 10:
    print("5 and 10 is not equal")
#Exercise 5
if 5 == 10 or 4 == 4
print("At least one of the statements is True")