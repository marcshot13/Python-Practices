"""We set a random number, then start a while loop that keeps running until the user input
and the random number match, while printing either they are aiming lower or higher"""

import random
random_number = random.randint(1,9)
user_number = 0

while random_number != user_number:
    user_number = int(input("Enter a number between 1 and 9: \n"))
    if random_number < user_number:
        print("Too high!")
    elif random_number > user_number:
        print("Too low!")
    else:
        print("Correct!")