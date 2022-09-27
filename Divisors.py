"""As usually, int the user input"""

user_number = int(input("Enter a number which you will be given it's divisors: "))

"""Now i make a list of every number until the user number + 1, because the last item doesnt show"""

x = range (1,user_number + 1)

"""Also, we create an empty list to add every divisor"""

divisors = []

"""We make a function such checks for every item in the range of the list if its remainder its 0, 
then it adds that number to a new list"""

def divisor_searcher (range,user_input,list_of_divisors):
    for i in range:
        if user_input % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors

"""Run the function and print the new list"""

divisor_searcher(x,user_number,divisors)
print(divisors)
