# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 10
CAR PARKING METER
You rummage through the coins in your pocket looking for the cash you need for the
parking meter which costs 60p per half-hour. Input the value of your coins in
pennies, line by line, with a -1 indicating your pocket is empty. Output the number of minutes that
you will be able to park for. [Note: you can only park in units of half-hours, nothing less.]
"""

def is_valid_coin(x):
    if x == -1 or x == 1 or x == 2 or x == 5 or x == 10 or x == 20 or x == 50 or x == 100 or x == 200:
        return True
    else:
        print("Please enter a valid coin (1, 2, 5, 10, 20, 50, 100, 200).")
        return False

money = 0
for i in range(10):
    coin = int(input())
    while not is_valid_coin(coin):
        coin = int(input())
    if coin == -1:
        break
    else:
        money = money + coin

parking_time = 30 * (money // 60)
print(parking_time)

    