#FINDING TEXT

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# For example,
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"

#write code bellow

first_app = text.find("zip", 0)
print text.find("zip", first_app + 1)

# ROUNDING NUMBERS

# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.14159

#write code bellow

new_value = x + 0.5
string = str(new_value)
decimal = string.find(".")
print string[:decimal]

#UNIT 2

# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(search,target):
	first = search.find(target)
	return search.find(target, first + 1)
    	


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
#>>> 25

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
#>>> 13


# UNIT 2 - BIGGEST
# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.


def biggest(a,b,c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

def bigger(a,b):
	if a > b:
		return a
	else:
		return b

def biggest(a,b,c):
	return bigger(bigger(a, b), c)

print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9


# UNIT 2 - Loops
# we check if i is smaller than 10, if it is it prints it, then executes
# the code bellow and checks if new value is smaller than 10, and prints it 
# until its true.
i = 0 
while i < 10:
	print i
	i = i + 1

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(a):
    i = 0
    while i != a:
        i = i + 1
        print i
    
print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

def print_numbers(a):
	i = 1
	while i <= a:
		print i
		i = i + 1
print_numbers(3)

# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
	result = 1
	while n >= 1:
		result = result * n
		n = n - 1
	return result

print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
