#PYTHON LIST
#Exersice 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#Exersice 2

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#Exersice 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Exersice 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#Exersice 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Exersice 6

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#Exersice 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#Exersice 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
#PYTHON TUPLES
#Exersice 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#Exersice 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#Exersice 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#Exersice 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
#PYTHON SETS
#Exersice 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Exersice 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Exersice 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Exersice 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Exersice 5

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#PYTHON DICTIONARIES
#Exersice 1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#Exersice 2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Exersice 3

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#Exersice 4

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Exersice 5

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
#PYTHON IF...ELSE
#Exersice 1
a = 50
b = 10
if a > b:
 print("Hello World")
#Exersice 2

a = 50
b = 10
if a != b:
 print("Hello World")
#Exersice 3
a = 50
b = 10
if a == b:

  print("Yes")
else:

  print("No")
#Exersice 4
a = 50
b = 10
if a == b:

  print("1")
elif a > b:

  print("2")
else:

  print("3")
#Exersice 5
if a == b and c == d:
  print("Hello")
#Exersice 6
if a == b or c == d:
  print("Hello")
#Exersice 7
if 5 > 2:
 print("Five is greater than two!")
#Exersice 8
if 5 > 2: print("Five is greater than two!")
#Exersice 9
print("Yes") if 5 > 2 else print("No")
#PYTHON WHILE LOOPS 
#Exersice 1
i = 1
while i < 6:

  print(i)
  i += 1
#Exersice 2

i = 1
while i < 6:
  if i == 3:
    break

  i += 1
#Exersice 3

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue

  print(i)
#Exersice 4
i = 1
while i < 6:
  print(i)
  i += 1
else:

  print("i is no longer less than 6")
  #PYTHON FOR LOOPS
  #Exersice 1
  fruits = ["apple", "banana", "cherry"]
for x in fruits:

  print(x)
  #Exersice 2
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue

  print(x)
  #Exersice 3
  
for x in range(6):
  print(x)
  #Exersice 4
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break

  print(x)