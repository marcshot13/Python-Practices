"""We ask the name of the person and age and store them as str and int respectively,
then we ask the current year and we store it as well"""

person_name = input("Enter your name: ")
person_age = int(input("Enter your age: "))
current_year = 2022

"""We make a function that subtracts the person age from the current year, then add 100 to it"""

def when_100_year_old(person_age,current_year):
    date_of_birth = current_year - person_age
    when_year_old = date_of_birth + 100
    return when_year_old

"""We print the result and a str since the retutn statement gives us an int"""

print("You will be 100 years old in "+ str(when_100_year_old(person_age,current_year)))