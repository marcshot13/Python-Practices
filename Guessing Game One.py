"""We set a random number, then start a while loop that keeps running until the user input
and the random number match, while printing either they are aiming lower or higher"""

"""For the first extra, we added that only if the player exits, the game ends, otherwise it keeps playing"""

"""Added a counter for number of guesses"""

import random
random_number = random.randint(1,9)
user_number = 0
number_of_guesses= 0

while random_number != user_number:
    user_number = input("Enter a number between 1 and 9, if you don't want to keep playing, type exit \n")
    number_of_guesses = number_of_guesses + 1
    if user_number.lower() == "exit":
        break
    elif random_number > int(user_number):
        print("Too low!")
    elif random_number == int(user_number):
        print("Correct!")
    if random_number < int(user_number):
        print("Too high!")

print("You guessed " + str(number_of_guesses) + " times")
