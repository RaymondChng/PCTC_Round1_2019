# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 2
DARTS
The maximum score you can achieve with three darts is 180. Input three whole
numbers each representing a dart score from a throw and output how much short of
the maximum the total of the darts thrown was.
"""

def is_valid_score(x):
    if x < 1 or x > 60:
        print("Please enter a score between 1 and 60 inclusive.")
        return False
    else:
        return True

score1 = int(input())
while not is_valid_score(score1):
    score1 = int(input())
score2 = int(input())
while not is_valid_score(score2):
    score2 = int(input())
score3 = int(input())
while not is_valid_score(score3):
    score3 = int(input())

short = 180 - score1 - score2 - score3
print(short)
