# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 8
PRINT A RUG
Kardeesh wants to 'print' out some rugs using her new 3D printer. Each rug will be
made out of stitched squares. A rug will be either 3, 4 or 5 squares wide and the length
of the rug will also be entered by the user. In this simulation she will use the character @ to
represent one square of the rug.
"""

def is_valid_width(x):
    if x < 3 or x > 5:
        print("Please enter a number between 3 and 5 inclusive.")
        return False
    else:
        return True

def is_valid_height(x):
    if x < 1 or x > 100:
        print("Please enter a number between 1 and 100 inclusive.")
        return False
    else:
        return True

rug_row = ""

width = int(input())
while not is_valid_width(width):
    width = int(input())

height = int(input())
while not is_valid_height(height):
    height = int(input())

for i in range(width):
    rug_row = rug_row + "@"

for i in range(height):    
    print(rug_row)

    