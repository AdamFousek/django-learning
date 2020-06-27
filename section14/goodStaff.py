# Printing in python / formatting
import re
item_one = "dog"
item_two = "cat"
x = "Item one: {} Item two: {}".format(
    item_one.capitalize(), item_two.capitalize())
# Variables
x = "Item one: {y} Item two: {z}".format(
    y="Adam", z="Eva")

# List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

firts_col = [row[0] for row in matrix]

# dictioneries
dic = {'test': 'value'}

# print(dic['test'])

#Tuple - immutable
# Sets - unique elements unordored

# Tuple
t = (1, 2, 3)

# print(t)

# Set

x = set()
x.add(1)
x.add(2)
# print(x)

test = set([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3])
# print(test)

# Control flow
d = {"Sam": 1, "Frank": 2, "Vito": 3}

# for key in d:
# print(key)
# print(d[key])

mypairs = [(1, 2), (3, 4), (5, 6)]

# for item in mypairs:
# print(item)

# Tuple unpacking
# for tup1, tup2 in mypairs:
# print(tup1)
# print(tup2)

# print(list(range(0,20,2)))

# for item in range(10):
# print(item)

# list comprehantion

x = [1, 2, 3, 4]

result = [num**2 for num in x]

# [1, 4, 9, 16]
# print(result)


def my_func(param1='default'):
    """
    THIS is the DOCstring
    """
    print("My first python function {}".format(param1))

# my_func()


def hello():
    return "hello"


def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1+num2
    else:
        return "Sorry, i need intergers!"


result = addNum("2", "3")

# Lambda Exprassion
mylist = [1, 2, 3, 4, 5, 6, 7]


def even_bool(num):
    return num % 2 == 0


evens = filter(lambda num: num % 2 == 0, mylist)

# print(list(evens))
"""
# Exceptions
try:
    f = open('test.txt', 'r')
    f.write("This is test")
except:
    print("Error: could not find file or read a data")
finally:
    print("Success")
    f.close()
"""


patterns = ['term1', 'term2']

text = 'This is a string with term1, not the other!'

match = re.search('term1', text)

# print(match.start())

split_term = '@'

email = 'user@email.com'

#print(re.split(split_term, email))

#print(re.findall('match', 'test phrase match in middle'))


def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Seraching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')


"""
test_phrase = 'sdsds..sssddd..sdddsddd...dsds...dssssss...sddddd'


test_patterns = ['sd*', 'sd+', 'sd?', 'sd{3}', 'sd{1,3}', 's[sd]+']
"""
test_phrase = 'This is a 4 string! But how can #i remove it. so?'


test_patterns = [r'\W+']

#multi_re_find(test_patterns, test_phrase)

s = "Global variable"

"""
def func():
    mylocal = 10
    print(locals())


func()
print(s)
"""


def hello(name="Jose"):
    print("the hello function has been run")

    def greet():
        return "This string is inside GREET"

    def welcome():
        return "This is string is inside welcome"

    if name == "jose":
        return greet
    else:
        return welcome


#x = hello()

# print(x())


def hello():
    return "Hi Jose"


def other(func):
    print("Hello")
    print(func())

# other(hello)


def new_decorator(func):

    def wrap_func():
        print("Code here before executing func")
        func()
        print("func() has been called")

    return wrap_func


def func_needs_decorator():
    print("This function is in need of a decorator")


#func_needs_decorator = new_decorator(func_needs_decorator)

# func_needs_decorator()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a decorator")


# func_needs_decorator()

