"""I take the list that has been given to us, and for every item in a, print those whose remainder
is equal to 0"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([a for a in a if a % 2 == 0 ])