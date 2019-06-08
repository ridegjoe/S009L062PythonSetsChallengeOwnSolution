# This challenge is my own solution, related to sets in Python.
# This was created by Tim Buchalka, Jean-Paul Roberts, Tim Buchalka's Learn Programming Academy:
# https://www.udemy.com/python-the-complete-python-developer-course/
#
# BEGINNING OF CHALLENGE (Tim Buchalka)
# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialize s string variable with the string.
#
# BEGINNING OF MY OWN CODE

vowels_tuple = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")
vowels_set = frozenset(vowels_tuple)

print("")
print(vowels_set)
print(sorted(vowels_set))
print("")

print(vowels_tuple)
print(sorted(vowels_tuple))
print("")

text = input("Type some text: ")
print(text)

characters_list = list(text)
print(characters_list)

characters_set = set(characters_list)
print(characters_set)

print("The following characters are not vowels: ")
print(characters_set.difference(vowels_set))
