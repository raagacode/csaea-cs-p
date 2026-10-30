# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp


def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi() # calling the fuction 
say_bye()
say_hi()
say_hi()
say_bye()

# Functions more commonly RETURN values, not merely print
# We can pass an ARGUMENT into a function's PARAMETER

def express_this(e): # e is called a PARAMETER, which is a placeholder for an ARGUMENT 
    return e

expression = express_this(3 + 2)# the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER

print(expression)

def greeter(name):
    return f"Hi {name}"

first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter("Hoppy")

print(first, second, third)

def remainder(a,b): 
    return a % b

result = remainder(10, 9)
print(result)

def is_far(distance):

    if distance >= 100:
        return "That's far"
    if distance < 100 and distance > 20:
        return "That's not too far"
    if distance <= 20:
        return "Hey that's pretty close by!"

#call is_far() on four different distances, and print the result
one = is_far(120)
two = is_far(63)
three = is_far(2)
four = is_far(1000000)

print(one, two, three, four)

# I want to create a function that doubles a number a bunch of times, then returns them as a list.
# Write a function named doubler(num, times) that has TWO parameters: 
# First parameter named 'num': the number I want doubled
# Second paramater named 'times':how many times we should double the number
# Tools to use: loops, lists[], .append(), *

def doubler(num, times):
    doubled_numbers = []
    number = num

    for n in range(times):
        number = number * 2
        doubled_numbers.append(number)

    print(doubled_numbers)
    return doubled_numbers

doubler(1, 5)

# Example output:
# doubler(1, 5)
# result --> [2, 4, 8, 16, 32]


# For Challenges 1 - 3, first write pseudocode, then solve in code.
 
# Challenge 1. 
# Make a calculator with 4 procedures that accept two arguments each. 
# 1) add any two numbers and print and return the result
# 2) subtract any two numbers and print and return the result
# 3) divide any two numbers and print and return the result
# 4) multiply any two numbers and print and return the result 

def adder(a, b):
    print(a + b)
    return a + b

sum = adder(1,3)
sum_two = adder(234,9)
print(sum)
print(sum_two)

# Challenge 2
# Make a function called 'average' that:
# 1) accepts five numbers
# 2) returns the average
# 3) print the returned value outside the function

# Challenge 3
# Make a function called is_even that:
# 1) accepts one number
# 2) prints "Even" if the number is even
# 3) prints "Odd" if the number is odd


# Challenge 4
# Use the pseudocode below to write code:
# Make a function called "analyze_word" that counts how many vowels and consonants are in a word
# Tools: uses a for loop, IF/THEN statement, "aeiou".

# The function analyze_word accepts one argument, a single word (string):
# Initialize two variables:
# vowelCount set to 0
# consonantCount set to 0
# Use a loop to iterate through each character in the word.
# Inside the loop, use an IF/ELSE statement:
# If the character is a vowel (a, e, i, o, u), increment vowelCount (increment means add 1 to vowelCount).
# Otherwise, increment consonantCount.
# After the loop ends: 
# 	return a f-string that states how many vowels and how many consonants are in the word.

# Call the function with a sample one-word string and print the returned result outside the function
