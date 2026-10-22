# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

# Boolean refresher:
# True or False
print(3==2) # <--- Not True
print(3==3) # <--- True

print(4!=6) # <--- True

# if 
num = 10
if num==10:
    print("Your number is 10")
else:
    print("Your number is not 10")

# if else
num = 5
if num <= 12:
    print("Yes, num is <= 12")
else:
    print("No your number is >= 12")

# if elif else
temp = 72
if temp > 72:
    print("ITS HOT!!")
elif temp >= 60:
    print("its noice!")
else:
    print("ITS COLD!!")


print()

x=2
y=20

if x == y:
    print(" x is equal to y")
elif x>=y:
    print("x is greater than y")
else:
    print('NOPE')

# Logical operators: and 
# Both sides of the 'and' must  be true, otherwise it's false. 
age = 16
has_permission = True

if age >= 16 and has_permission: 
    print("You can drive")
else:
    print("You can't drive yet")

# Logical operators: 'or' and 'not'

day = "Sunday"
if day == "Saturday" or day== "Sunday":
    print("Its a weekend:)")
else:
    print("Its a weekday:(")

if day is not "Monday":
    print("Its not monday, THANK GOSH")


# Challenge 1
# Ask the user for their age. 
# If under 13, “You can watch PG or G movies.”
# If 13–17, “You can watch PG-13 movies.”
# If 18+, “You can watch any movie.”
# Example output:
# Enter your age: 15
# You can watch PG-13 movies.
age = input("How old are you ")
age = int(age)

if age < 13:
    print("You can watch PG or G movies")
elif age <= 13:
    print("You can watch PG-13 movies")
elif age >= 18:
    print("You can watch any movie")

# Challenge 2
# Challenge 2: Leap Year
# Rules:
#   - Years divisible by 4 are leap years...
#   - ...unless they're divisible by 100, then they're NOT leap years...
#   - ...unless they're also divisible by 400, then they ARE leap years.
# Example output:
# Enter a year: 1900
# 1900 is not a leap year.
# (Test: 2024 -> leap, 1900 -> not, 2000 -> leap)
# These are all leap years: 1600, 1692, 1996, 2000, 2004, 2020, and 2024

year= input("Enter a year")

year= int(year)
if year/400==0:
    print("Leap year")
elif year/4 ==0:
    print("Leap Year")

