import random
winner = 0
def replay_win(condition_variable):
    play_again = int(input("You win! Would you like to play again? \n 1 for yes \n anything else for no: \n"))
    if play_again != 1:
        condition_variable =+ 1
    return condition_variable

def replay_lose(condition_variable):
    play_again = int(input("You lose! Would you like to play again? \n 1 for yes \n anything else for no: \n"))
    if play_again != 1:
        condition_variable = + 1
    return condition_variable

def replay_draw(condition_variable):
    play_again = input("It's a draw! Would you like to play again? \n 1 for yes \n anything else for no: \n")
    if play_again != "1":
        condition_variable = + 1
    return condition_variable

while winner == 0 :
    user_choice = int(input("Enter your input (a number) \n 1.Paper \n 2.Rock \n 3.Scissors: \n "))
    system_random_choice = random.randint(1,3)
    if user_choice == 1 and system_random_choice == 2:
        winner = replay_win(winner)
    elif user_choice == 1 and system_random_choice == 3:
        winner = replay_lose(winner)
    elif user_choice == 1 and system_random_choice == 1:
        winner = replay_draw(winner)
    elif user_choice == 2 and system_random_choice == 3:
        winner = replay_win(winner)
    elif user_choice == 2 and system_random_choice == 1:
        winner = replay_lose(winner)
    elif user_choice == 2 and system_random_choice == 2:
        winner = replay_draw(winner)
    elif user_choice == 3 and system_random_choice == 1:
        winner = replay_win(winner)
    elif user_choice == 3 and system_random_choice == 2:
        winner = replay_lose(winner)
    elif user_choice == 3 and system_random_choice == 3:
        winner = replay_draw(winner)
    else:
        print("Not a valid number")