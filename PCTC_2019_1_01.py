# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 1
NAME CHANGE
What name would you like to have been given? In this challenge you will input two
names (on separate lines) which will represent your current name and what you
would like to be called. You will then output an official name-changing statement of the form:
Hello <name1>, your name is now <name2>.
"""

def is_valid_name(name):
    if len(name) < 1 or len(name) > 30:
        print("Please enter a name between 1 and 30 characters inclusive.")
        return False
    else:
        return True

name1 = input()
while not is_valid_name(name1):
    name1 = input()
name2 = input()
while not is_valid_name(name2):
    name2 = input()

print("Hello " + name1 + ", your name is now " + name2 + ".")