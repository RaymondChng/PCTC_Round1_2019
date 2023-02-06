# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 7
FOLLOW MY SISTER
Jack has an older sister Amy and he often likes to be a bit annoying. Their mum is
coming home with four cakes, one lemon, one chocolate, one caramel and one coffee. If
Jack gets asked first he will say he wants chocolate but if Amy gets asked first then he
will say he wants the same cake that Amy picks unless Amy picks coffee (which he hates) in which
case he will say chocolate.
The first input will be 1 or 2 where 1 indicates that Jack gets asked first and 2 indicates that Jack
gets asked second.
If the first input is 2 then (and only then), there will be a second input which indicates Amy's
response which will be either the word lemon or the word chocolate or the word caramel or the
word coffee.
Output what Jack will ask for in this circumstance again as a single word either
lemon/chocolate/caramel/coffee.
"""

asked = int(input())
if asked == 1:
    jack_choice = "chocolate"
    print(jack_choice)

if asked == 2:
    amy_choice = input()
    if amy_choice == "coffee":
        jack_choice = "chocolate"
    else:
        jack_choice = amy_choice
    print(jack_choice)
