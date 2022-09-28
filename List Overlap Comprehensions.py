"""From what i read it cannot be made in 1 line, so ill do them as i could and the other way"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
c.append(print([x for x in a if x in b and x not in c]))

d=[]

"""This is the not one liner"""

for number in a:
    if number in b and number not in d:
        d.append(number)

print(d)