# Variables store any kind of info
# Make sure to use descriptive variable names
#Note that variables can be overwritten.



    #   1b |  2b |  1b |  4b | 8b |  4by   
#name| age   height 
#value| 74   3.2
#addr| %&54  (^36*)


password="Hellloooo"
email="r@k"
print("Password:/t",password, "\nemail:\t\t", email)

#variable name convention for boolean
isComplete=False
isEnabled=False
isAwake=True
# math conventions
x = 3.14
y = 8
(print(x + y))

# variables are flexible. you create or update another variable, like so:
count = 10 
print(count)
count_down = count - 1
print(count_down)

#  Change x,y, and z to something meaningful
Name = "Radia Perlman"
Years_of_employment= 34
Job="Networking engineer"

print(f"This is {Name}. She has been working as a {Job} for {Years_of_employment} years")

# Challenge 2: Update Variables  
# Create a variable called 'count' with a value of 10.  
# Use another variable to increase 'count' by 5
# Print the result

count=10
print(count)
count_down= count + 5
print(count_down)





# Challenge 3: Swap Variables  
# Given variables num = 4 and y = "hello".  
# Swap the values so that num = "hello" and y = 4. 
# Use a temporary variable.  
# Hint: You will need to create one new variable. 

num=4
y="hello"
extra= "temp"
extra=num
num= y
y=extra
print(num)
print(y)
