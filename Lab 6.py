#DIR-FILES.MD
#Exercise 1


import os

path = input("Enter your path:")


print("Directories:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)


print("\nFiles:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)


print("\nAll Directories and Files:")
for item in os.listdir(path):
    print(item)

#Exercise 2
import os

path = 'Nothing.txt'



if os.path.exists(path):
    print("Path exists")
else:
    print("Path does not exist")


if os.access(path, os.R_OK):
    print("Path is readable")
else:
    print("Path is not readable")



if os.access(path, os.W_OK):
    print("Path is writable")
else:
    print("Path is not writable")


if os.access(path, os.X_OK):
    print("Path is executable")
else:
    print("Path is not executable")
#Exercise 3
'''Write a Python program to test whether a given path exists or not. If the path exist find the
 filename and directory portion of the given path. '''
import os

path = 'Nothing.txt'


if os.path.exists(path):
    print("Path exists")

   
    dirname = os.path.dirname(path)
    filename = os.path.basename(path)

    print("Directory:", dirname)
    print("Filename:", filename)

else:
    print("Path does not exist")
#Exercise 4
'''Write a Python program to count the number of lines in a text file.'''
import os


file = open('Nothing.txt')
lines = file.readlines()
total_lines = len(lines)
print("The total is: ", total_lines)
# import os

# def count_lines(filename):
#     with open(filename) as file:
#         lines = file.readlines()
#         total_lines = len(lines)
#         return total_lines


# count = count_lines('Triangle.py')
# print("The total lines are: ", count)

#Exercise 5
''' Write a Python program to write a list to a file. '''
import os
my_list = ["My", "name", 'is', 'Shakhzod']

with open("Nothing.txt", "w") as file:
    for item in my_list:
        file.write(item+'\n')
#Exercise 6
import string

for letter in string.ascii_uppercase:
    filename = letter + ".txt"
    with open(filename, "w") as file:
        file.write("This is file " + filename)
#Exercise 7
''' Write a Python program to delete file by specified path. Before deleting check for access
 and whether a given path exists or not.'''
import os

path = 'Nothing.txt'

if os.access(path, os.R_OK):
    print("Path is readable.")
else:
    print("Path is not readable.")


if os.path.exists(path):
    print("This file exists.")
else:
    print("This file does not exist.")


os.remove('Nothing.txt')
#PYTHON BUILTIN FUNCTION EXERCISES
#Exercise 1
'''Write a Python program with builtin function to multiply all the numbers in a list'''
import functools

list = [1, 2, 3, 4, 5]

x = functools.reduce(lambda a, b: a * b, list)

print("The sum is:", x )
#Exercise 2
'''Write a Python program with builtin function that accepts a string and calculate the number 
of upper case letters and lower case letters'''
def count_the_letters(s):
    upper = 0
    lower = 0
    for l in s:
        if l.isupper():
            upper += 1
        elif l.islower():
            lower += 1

    return upper, lower
    

s = "My name is Shakhzod"
result = count_the_letters(s)
print(result)
#Exercise 3
def is_palindrome(s):
    if(s == s[::-1]):
        return("String is palindrome")
    else:
        return("String is not palindrome")


s = input("Enter your string: ")
print(is_palindrome(s))
#Exercise 4
import time
import math


def calculate_sqrt(number):
    return math.sqrt(number)


number = 25100
delay_ms = 2123

time = (delay_ms / 1000)


result = calculate_sqrt(number)


print(f"The square root of {number} is {result}")
#Exercise 5
def all_true(tuple):
    return all(tuple)


tuple = (True, True, True, True)
if all_true(tuple):
    print("All elements of the tuple are true.")
else:
    print("Not all elements of the tuple are true.")




  








