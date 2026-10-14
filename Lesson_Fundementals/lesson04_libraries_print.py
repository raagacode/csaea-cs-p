# PYTHON LIBRARIES

# Doc on libraries: https://docs.python.org/3/library/index.html   
# Doc on Math library: https://docs.python.org/3/library/math.html


import math # <--- for math library

sq_root = math.sqrt(25)  #<--- sqrt is the python math term for sqare root
print("sqare root:", sq_root)

round_up = math.ceil(4.5) # <--- math.ceil rounds the number up
print("Round up: ", round_up)

round_down = math.floor(4.8)
print(f"Round down: {round_down}")

exponent= math.pow(2,3) # 2 is base and 3 is the exponent
print(exponent)

# CONSTANT VARIABLES- a variable that never changes
# pi is a constant
PI=math.pi # <--- when the variable name is full uppercse, you know it is a constant.
print(PI)
# 64 bytes is max for 1 float



 # Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

diameter=14
radius= (diameter) / 2
Area= math.pi * math.pow(radius,2)
print(Area)

# PYTHON RANDOM LIBRARY
# Python's library is a Pusudorandom Number Generator

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 

# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 

# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 

# Use math library to round the float UP to an integer. 

# BONUS CHALLENGE: Make your random number output between 1 and 10. 
#______________________________________________________________________
# RANDOM NUMBER GENERATOR
seed=7
num1=math.pow(seed,7)

num2=math.pi*seed

num3=math.sqrt(seed)

print(math.ceil(num1))

print(math.ceil(num2))

print(math.ceil(num3)) # <--- this is for multiple random numbers

# You can also do this way too
seed = 345.87
step1 = seed / 6.7
step2 = step1 - 800
step3 = step2 % 10
result = math.ceil(step3)
print("Your random num is:", result)


#CHALLENGE 1 

print("\nChallenge 1:")

diameter = 14
radius = diameter/2
circle_area = math.pi*math.pow(radius,2)
print(circle_area)
print(math.ceil(circle_area))
print("\n")

print("Challenge 3:")
#Simulate rolling a six sided dice
import random

die_roll = random.randint(1,6)
print(f"You rolled a: {die_roll}")


#Challenge 4

num = random.randint(1,75)
calc1 = math.sqrt(num)
calc2 = math.ceil(calc1)
print(f"Unrounded square root: {calc1}\nRounded square root: {calc2}")


# challenge 5


base = random.randint(1,6)
exponent = random.randint(1,6)
equation = base**exponent
result = int(equation)
print(f"Result: {result}")

