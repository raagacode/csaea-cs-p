# Key Consepts
add=7+2
print("Sum:", add)
subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product", multiply)

float_divide=7/2
print("Float Division:", float_divide)
# 24 byts = float
float_divide_divide= 10/3
integer_divide= 7//2
print("Integer division", integer_divide)
# mod or % or modulous means the remainder
mod= 7%2 
print("Modulus:", mod)

exponent= 7 ** 2
print("Exponent", exponent)


# PEMDAS (parenthases, exponents, muliply, divide, addition, subtract)
# Python uses pemdas!!
result1= 2 + 3 * 4
print("Result 1 is:", result1)

result2 = 2+4**6
print("Result 2 is:", result2)


# !CHALLENGES!
#Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.
# Create seperate variables for width, height, and result.
width=8
length=5
result = print("result is:",width * length)


# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. 
# (Use 3.14 for π.)  

pi= 3.14
radius=7
print("The Area Is:", pi*radius**2)

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks. 

cost_or_book= 12.99
cost_of_notebook=3.50
total = (12.99 * 3) + (3.50*4)
print("The total cost is:",total)
 #Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd. 
number = 57
problem = number%2

if problem == 1:
    print("Odd")
else:
    print("Even")