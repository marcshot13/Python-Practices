"""We import random"""

import random

"""The exercise gives us two lists"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

"""We make another list to store the common values"""

c = []

"""We check that for every item of the first list, if its contained in the second, to add that item in the
third list, only if only that item is not already contained"""

def join_of_lists(list_a,list_b,list_c):
    for number in list_a:
        if number in list_b and number not in list_c:
            list_c.append(number)
    return list_c

"""We run the function and print it"""

join_of_lists(a,b,c)
print(c)
