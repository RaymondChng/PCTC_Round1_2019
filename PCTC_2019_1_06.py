# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 6
LEMONADE STAND
John went shopping to buy lemons and sugar to make lemonade but he forgot to check
his ingredients. He NEEDS at least 20 lemons and 3kg of sugar.
Input the number of lemons he bought followed by the number of kgs of sugar he bought (both will
be whole numbers) and then display one of the following options:
A if John has enough ingredients
B if he needs more lemons
C if he needs more sugar
D if he needs both more sugar and lemons.
"""

def is_valid_num(x):
    if x < 1 or x > 100:
        print("Please enter a number between 1 and 100 inclusive.")
        return False
    else:
        return True
        
lemon = int(input())
while not is_valid_num(lemon):
    lemon = int(input())

sugar = int(input())
while not is_valid_num(sugar):
    sugar = int(input())

if lemon > 20 and sugar > 3:
    print("A")
elif lemon <= 20 and sugar > 3:
    print("B")
elif lemon > 20 and sugar <= 3:
    print("C")
else:
    print("D")