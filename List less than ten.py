"""List provided by the exercise"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""User input for number"""

user_number = int(input("Enter a number: "))

"""Made an empty list to store the values of the lesser than 5 items in the list"""

z = []

"""Made a for loop to check wether every item in the list one by one was less than five"""

def point_less_than_five(list,user_input):
    for i in list:
        if i < user_input:
            z.append(i)

"""Ran the function and printed the result"""

point_less_than_five(a,user_number)
print(z)