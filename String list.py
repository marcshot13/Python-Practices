"""We ask for string input"""

user_str = input("Escriba alguna palabra: ")

"""We reverse the string, using list notation as a string is a list itself. For reversing the string we
use [(starting point of such list):(ending point of such list:(additional effect)] if we use -1 we reverse
the order of the list, in case of a string, reverses the position of such string"""

reverse_string = user_str [::-1]

"""We make the condition so if the word is equal to its reverse state, print that is a palindrome, otherwise
print that it isnt"""

if user_str == reverse_string:
    print("The string is palindrome")
else:
    print("The String is not palindrome")