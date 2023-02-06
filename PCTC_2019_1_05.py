# Perse Coding Team Challenge 2019
# Round 1
# Practice Attempt by Raymond Chng

"""
Question 5
FOX IN A HOLE
There are 7 holes labelled from 1 to 7. A fox is hiding in one of the holes. Your job is
to report the whereabouts of the fox which is shown as an F. An empty hole is
represented by a capital letter O.
"""

seq = input()
for i in range(len(seq)):
    if seq[i] == "F":
        print(i+1)