"""List provided by the exercise"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""Made a for loop to check wether every item in the list one by one was less than five"""

def point_less_than_five(list):
    for i in list:
        if i < 5:
            print(i)

"""Ran the function"""

point_less_than_five(a)