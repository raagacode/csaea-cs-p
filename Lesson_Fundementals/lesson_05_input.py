# String fromating and concatonation


greeting = "Hello"
first_name = "Ada"
#Option 1
print(greeting, first_name)
#Option 2
print(greeting + first_name)
# Option
print(f"{greeting} {first_name}")

#        0    1    2
    #   ⬇    ⬇   ⬇
list = ["2", "q", "c"]

greeting = "hello"
second_letter = greeting[1]
print (second_letter)

# Sting indexing and slicing

word = "super-cali-fragil-istic-expi-ali-docious"
print(word)
print("/nThe word is,:, word")


# what if i wanna grab only the first letter of the word?
print("The First letter is:,[0]")


# what if i wanna grab only the last letter of the word?
print("The last letter is:, [-1]")

# for slicing use :
print("Range of letters (non-inclusive:)", word[3:7])

print("First 5 letters:", word[:5])

print("Everything after the first 5 letters", word[5:])

print("Last seven letters:", word[-7:])  

print("Step through every second character:", word[0:0:2]) #<--- or [::2] also works

print("Strings in reverse", word[::-1])


# len shows the length of how many characters there are
length= len("ASCII")
print(length)
# The len option will also count spaces too!
length_2= len("    LOVELACE")
print(length_2)


#______________________________________________________________________________#

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

quote = input("Enter your fav quote ")

length = len(quote)
print(length)


# Challenge 2:
# Ask the user to enter a word that is at least 7 characters long. 
# Print the 2nd through 6th characters.
# Use string slicing.

question = input("Enter a word that is at least 7 characters long! ")

print("2nd through 6th letters:", question[2:7])



# Challenge 3: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation or f-strings.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Formatted name: Lovelace, Ada

Ask = input("What is your first name? ")
Ask_2 = input("What is your last name? ")
print(f"Hello {Ask_2}, {Ask}")
#___________________________________________________________________________________________________________________#

