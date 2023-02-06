# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 3
HELP YOURSELF
If you are offered a slice of cake and you are hungry then chances are you might pick
the one that looks largest. In this challenge you will be given the volume (in cubic
centimetres) of two slices of cake, SLICE 1 and SLICE 2 in that order.
"""

def is_valid_volume(x):
    if x < 1 or x > 1000:
        print("Please enter a volume between 1 and 1000 inclusive.")
        return False
    else:
        return True

vol1 = int(input())
while not is_valid_volume(vol1):
    vol1 = int(input())
vol2 = int(input())
while not is_valid_volume(vol2):
    vol2 = int(input())

if vol1 > vol2:
    print("SLICE 1")
elif vol2 > vol1:
    print("SLICE 2")
else:
    print("SAME")
