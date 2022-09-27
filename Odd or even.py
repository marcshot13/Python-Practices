"""We ask the user for a number and we save it as an it"""

user_number = int(input("Give me a number: "))

"""We do a function to check if the modulus operation or remainder of dividing by 2 is:
if the modulus is 0, this means the int is even, if the modulus is 1, the number is odd"""

def odd_or_even(input_number):
    input_number = input_number % 2
    if input_number == 0:
        print("Your number is an even number")
    else:
        print("Your number is an odd number")

"""We apply the function to the user number"""

odd_or_even(user_number)