# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 9
SEASON JUMPING
We all know, of course, that our seasons go in the cycle spring - summer - autumn -
winter and then back to spring again. Input a current season and then the number of
seasons to jump and output the season that it will then be.
"""

def is_valid_num(x):
    if x < 0 or x > 100:
        print("Please enter a positive integer less than 100.")
        return False
    else:
        return True

season_list = ["spring", "summer", "autumn", "winter"]
curr_season = input()
jump = int(input())
while not is_valid_num(jump):
    jump = int(input())

for i in range(4):
    if season_list[i] == curr_season:
        season_num = i+1

new_season_num = (jump + season_num - 1) % 4

print(season_list[new_season_num])

    