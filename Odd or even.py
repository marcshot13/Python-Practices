"""We ask the user for a number and we save it as an it"""

user_number = int(input("Give me a number: "))

"""We do a function to check if the modulus operation or remainder of dividing by 2 is:
if the modulus is 0, this means the int is even, if the modulus is 1, the number is odd"""
"""We add as the extra says to check if the number is multiple by 4, adding an extra message
in case it is"""

def odd_or_even(input_number):
    if input_number % 2 == 0 and input_number % 4 != 0:
        print("Your number " + str(input_number) + " is an even number")
    elif input_number % 2 == 0 and input_number % 4 == 0:
        print("Your number " + str(input_number) + " is multiple of 4 and even at the same time")
    else:
        print("Your number " + str(input_number) + " is an odd number")



"""We apply the function to the user number"""

odd_or_even(user_number)