# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 4
EQUALLY SPACED?
A simple sequence can be spotted because it changes by the same number each
time. For example 12 16 20 24 changes by 4 each term and 17 14 11 8 changes
by -3 each term.
Input four whole numbers on four lines and output NO (uppercase) if it is not a simple sequence or
otherwise output the number that it changes by each time.
"""

def is_valid_num(x):
    if x < -1000 or x > 1000:
        print("Please enter a number between 1 and 1000 inclusive.")
        return False
    else:
        return True

num1 = int(input())
while not is_valid_num(num1):
    num1 = int(input())
num2 = int(input())
while not is_valid_num(num2):
    num2 = int(input())
num3 = int(input())
while not is_valid_num(num3):
    num3 = int(input())
num4 = int(input())
while not is_valid_num(num4):
    num1 = int(input())

diff1 = num4 - num3
diff2 = num3 - num2
diff3 = num2 - num1

if diff1 == diff2 and diff2 == diff3:
    print(diff1)
else:
    print("NO")
    
