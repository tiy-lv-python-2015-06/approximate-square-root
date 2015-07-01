#Write a program that asks the user for one or more sentences
#and then lets the user know if it is a palindrome

#ask the user for input

import re

def clean_up(user_input):
    """This is to clean up the input"""
    user_string_clean = re.sub(r'[^A-Za-z]','', user_input)
    return user_string_clean

def palindrome_check(user_input):
    """This is checking the the users input iteratively for a palindrome. """
    if user_input[::-1] == user_input:
        return True
    else:
        return False


# Take the user_input and lowercase everything
user_input = input("Enter a sentence here ").lower()


if (clean_up(user_input)) and (palindrome_check(user_input)):
    print(" is a palindrome!!!")
else:
    print(" is not a palindrome.")



#Function 1 I need to take the user input and stirp it of all puncutation,
# white space, and make everything lower case


#Function 2 I need to test the string to check if it is a palindrome or not

#Function 3 print out weather or not it is a palindrome.
