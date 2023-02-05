#Ex 1

n = int(input())
def to_gramm(num_of_gramm):
    return num_of_gramm * 28.3495231


print(to_gramm(n))


#Ex 2
n = int(input("enter: "))
def my_temp(f):
    x = (5 / 9) * (f - 32)                            #(5 / 9) * (f – 32)
    return x


print('answer',my_temp(n))
#Ex 3   
'''3.Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
If all 35 animals were chicken then we’d have 2*35 =70 legs. 
The extra 94 - 70 = 24 legs belong to 24/2 = 12 rabbits, the others 35 - 12 = 23 are chickens.'''
def solve(numheads, numlegs):
    legs = numheads * 2
    print(legs)
    rabbit = (numlegs - legs) // 2
    print(rabbit)
    chicken = numheads - rabbit
    print(chicken)
    return rabbit, chicken


print(solve(35, 94))
#Ex 4
def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, (num//2) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]

print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8]))
#Ex 5
word = input()


def permute(word, l, r):
    if l == r:
        print("".join(word))
    else:
        for i in range(l, r):
            word[l], word[i] = word[i], word[l]
            permute(word, l + 1, r)
            word[l], word[i] = word[i], word[l]


permute(list(word), 0, len(word))
#Ex 6
str = input()


def rev(str):
    str = list(str.split(" "))
    str.reverse()
    return " ".join(str)


print(rev(str))
#Ex 7

x = input().split()



def has_33(x):
    p = False
    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            if int(x[i]) == 3:
                p = True
                break

    return p


print(has_33(x))
#Ex 8
def spy_game(x):
    zero1 = x.index(0)
    zero2 = x.index(0, zero1 + 1)  
    seven = x.index(7)
    if x[zero1:zero2] != seven and seven > zero2:
        return True

    return False

print(spy_game([1,2,4,0,0,7,5]))
#Ex 9
import math

def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

print(sphere_volume(5))
#Ex 10
def unique_list(lst):
    unique_el = []
    for el in lst:
        if el not in unique_el:
            unique_el.append(el)
    return unique_el
    #Ex 11
    str = input()
def is_palindrome(str):
    str = str.replace(" ", "")
    return str == str[::-1]


print(is_palindrome(str))
#Ex 12
lis = list(input().split())


def histogram(nums):
    for i in range(len(nums)):
        print("*" * int(nums[i]))


histogram(lis)
#Ex 13
import random

def guess_the_number():
    number = random.randint(1, 20)
    name= (input("Hey,what is your name? \n"))
    print(" Ok, " + name + ". I'm thinking of a number between 1 and 20. Can you guess what it is?")
    while True:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print("You got it! The number was", number)
            break

guess_the_number()
#CLASSES
#Ex 1
class String:                                                    
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter a string: ")

    def printString(self):
        print(self.str.upper())


s = String()
s.getString()
s.printString()
#Ex 2
#Ex 3

class Shape:
    length = 0

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return pow(self.length, 2)


figure1 = Shape()

figure2 = Square(3)

print(figure2.area())
#Ex 3
class Rectangle(Shape):
    width = 0

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width


figure3 = Rectangle(5, 6)


print(figure3.area())
#Ex 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point coordinates: ({}, {})".format(self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)



p1 = Point(0, 0)
p2 = Point(3, 4)

p1.show()
p2.show()



print("Distance between points:", p1.dist(p2))
#Ex 5
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit accepted. Current balance:", self.balance)
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal accepted. Current balance:", self.balance)
#Ex 6
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", primes)
#FUNCTIONS2
#Ex 1
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]



def choose_movie(movie):
    for i in range(len(movies)):
        if movies[i]['name'] == movie:
            if movies[i]['imdb'] > 5.5:
                return True

    return False


print(choose_movie('Love'))
#Ex 2
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

def choose_movie_list():
    list = []
    for i in range(len(movies)):
        if movies[i]['imdb'] > 5.5:
            list.append(movies[i]['name'])
    return list

print(choose_movie_list())
#Ex 3
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


def movie_category(category):
    l = []
    for i in range(len(movies)):
        if movies[i]['category'] == category:
            l.append(movies[i]['name'])
    return l


print(movie_category('Comedy'))
#Ex 4
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]



def avarage_imdb(str):
    sum = 0
    count = 0
    for i in range(len(movies)):
        for el in str:
            if movies[i]['name'] == el:
                sum += movies[i]['imdb']
                count +=1

    return sum/count

print(avarage_imdb(['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']))
print(['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two'])
#Ex 5
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]



def avarage_category_imdb(category):
    list = []
    sum = 0
    count = 0
    for i in range(len(movies)):
        if movies[i]['category'] == category:
            list.append(movies[i]['name'])

        for el in list:
            if movies[i]['name'] == el:
                sum += movies[i]['imdb']
                count += 1

    return sum / count


print(avarage_category_imdb('Romance'))




