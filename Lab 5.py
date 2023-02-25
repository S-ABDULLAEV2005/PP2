#Python RegEx exercises
#Exercise 1
import re

string = input("Enter a string: ")

pattern = r'a[b]*'

matches = re.findall(pattern, string)

if len(matches) > 0:
    print(f"Found {len(matches)} match(es):")
    for match in matches:
        print(match)
else:
    print("No matches found.")
#Exercise 2
import re

string = input("Enter a string: ")

pattern = r'a[b]{2,3}'

matches = re.findall(pattern, string)

if len(matches) > 0:
    print(f"Found {len(matches)} match(es):")
    for match in matches:
        print(match)
else:
    print("No matches found.")
#Exercise 3
import re

string = input("Enter a string: ")

pattern = r'[a-z]+_[a-z]+'

matches = re.findall(pattern, string)

if len(matches) > 0:
    print(f"Found {len(matches)} match(es):")
    for match in matches:
        print(match)
else:
    print("No matches found.")
#Exercise 4
import re

string = input("Enter a string: ")

pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, string)

if len(matches) > 0:
    print(f"Found {len(matches)} match(es):")
    for match in matches:
        print(match)
else:
    print("No matches found.")
#Exercise 5
import re

string = input("Enter a string: ")

pattern = r'a.*b$'

match = re.search(pattern, string)

if match:
    print("Match found:")
    print(match.group())
else:
    print("No match found.")
#Exercise 6
import re

string = input()

pattern = re.sub("\s", ":",   string)

print(pattern)
#Exercise 7
import re

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('python_exercises'))
#Exercise 8
import re

def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)

string = input("Enter a string: ")

result = split_at_uppercase(string)

print("Result:")
print(result)
#Exercise 9
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)


print(capital_words_spaces("PythonExercisesPracticeSolution"))
#Exercise 10
import re

def camel_to_snake(text):
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake('PythonExercises'))

 