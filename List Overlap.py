"""We import random"""

import random

"""We create two empty lists to be randomised"""

a_random = []
b_random = []

"""We randomise the range of each list, to make it wild"""

rango1 = random.randint(30,80)
rango2 = random.randint(80,120)
rango3 = random.randint(20,60)
rango4 = random.randint(60,99)

"""We randomise every item in every random range in both lists"""

def random_list(range1,range2,list):
    for i in range(range1,range2):
        n = random.randint(1,75)
        list.append(n)
    return list

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

random_list(rango1,rango2,a_random)
random_list(rango3,rango4,b_random)
print(sorted(a_random))
print(sorted(b_random))
join_of_lists(a_random,b_random,c)
print("\n", c)
