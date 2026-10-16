#  f-strings
name="Ada"
last_name="lovelace"
print(f"Hello {name} {last_name}!")

#Concatenation:
print("Hello" + " " + name + " " + last_name + "!")

character = "SpOnGeBoB SqUaRePAnTs"
print("/nLovercase:", character.lower())
#This code makes all the words lowercase

print("/n:", character.upper())
# This makes all letters uppercase

print("Capitalize first letter:", character.capitalize())
#This capatalizes the first letter!

print("Title format:", character.title())
# This makes the word into a standard title format

print() #<--- Gives an empty line
sentence = "Goofy, goofy goober."
new_sentence= sentence.replace("goofy", "your")
print(sentence)
print(new_sentence)

#____________
# JOIN AND SPLIT
groceries = "milk, eggs, bread, butter, peanuts"
print("/nOriginal stiring:", groceries)

# split the string into a python list
items= groceries.split(",")
print(items)
# Now, all of these turn into their own variables

# Joining a list back together into a sting:
joined= " and ".join(items) #<--- Dont forget space between quotes in between and
print(joined)
print(type(items)) #<---- This is the list
print(type(joined)) #<--- This is with the string


# Challenge 3: Word Mutation
# Ask for a word and print it backwards, in uppercase, and lowercase.
# Example output
# Enter a word: Python
# Uppercase: PYTHON
# Lowercase: python
# Backwards: nohtyP

python= "Python"
print("\n:", python.upper())
print("\n:", python.lower())
print("\n:", python[::-1])