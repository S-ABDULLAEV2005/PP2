#PYTHON MATH
#Exercise 1
import math
n = int(input())

x = math.radians(n)
print(x)
#Exercise 2
import math
b1 = int(input())
b2 = int(input())
h = int(input())

x = 0.5 * (b1 + b2) * h

print(x)
#Exercise 3
from math import tan, pi
sides = int(input())
length = float(input())
area = sides * (length ** 2) / (4 * tan(pi / sides))
print(area)
#Exercise 4
import math
base = float(input())
height = float(input())
area = base * height
print(area)
#PYTHON ITERATORS AND GENERATORS
#Exercise 1
n = int(input())
def generate_squares(x):
   
    for i in range(1, x + 1):
        yield i**2
for square in generate_squares(n):
    print(square)

#Exercise 2
n = int(input("Enter a number: "))

def generate_even_numbers(n):
    for i in range(2, n+1, 2):
        yield i


even_numbers = generate_even_numbers(n)

print(",".join(str(number) for number in even_numbers))

#Exercise 3
x = int(input())
def generate_divisible_by_3_and_4(n):
    
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for number in generate_divisible_by_3_and_4(x):
    print(number)

#Exercise 4
a = int(input())
b = int(input())
def squares(x, y):
   
    for i in range(x, y + 1):
        yield i**2
for square in squares(a, b):
    print(square)

#Exercise 5
x = int(input())
def countdown(n):
   
    while n >= 0:
        yield n
        n -= 1
for number in countdown(x):
    print(number)

#PYTHON DATE
#Exercise 1
from datetime import datetime, timedelta


current_date = datetime.now()


new_date = current_date - timedelta(days=5)
new_date_str = new_date.strftime('%Y-%m-%d')

print('Five days ago from today was:', new_date_str)

#Exercise 2
from datetime import datetime, timedelta

today = datetime.now()
yes = today - timedelta(days=1)
tom = today + timedelta(days=1)
print("Yesterday was: ", yes)
print("Today is: ", today)
print("Tomorrow will be: ", tom)

#Exercise 3
from datetime import datetime
dt = datetime.now()
dt_without_microseconds = datetime.strptime(dt.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

print('Datetime without microseconds:', dt_without_microseconds)

#Exercise 4
from datetime import datetime
date1 = datetime(2022, 2, 14, 12, 0, 0)
date2 = datetime(2022, 2, 15, 12, 0, 0)
difference_in_seconds = (date2 - date1).total_seconds()

print('The difference between the two dates in seconds is:', difference_in_seconds)
#PYTHON JSON PARSING
#Exercise 1
import json

file = open('sample-data.json', 'r')
s = file.read()
file.close()
d = json.loads(s)
imdata = d['imdata']

print("""
Interface Status
================================================================================
DN                                                 Description           Speed      MTU
-------------------------------------------------- -------------------   ------    ------""")

for item in imdata:
    print(item['l1PhysIf']['attributes']['dn'], end='\t')
    print(item['l1PhysIf']['attributes']['descr'], end='\t'*7)
    print(item['l1PhysIf']['attributes']['speed'], end='\t'*2)
    print(item['l1PhysIf']['attributes']['mtu'])