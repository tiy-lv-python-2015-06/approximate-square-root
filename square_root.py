# Write a program that asks the user for a positive
# number and then outputs the approximated square root
# of the number. Use Newton's method to find the square
# root, with epsilon = 0.01. (Epsilon is the allowed error,
# plus or minus, when you square your calculated square
# root and compare it to your original number.)

def find_sq_root(number):
    # count starts at 1
    count = 1

    # our guess starts at 1
    guess = 1

    while True:
        average = (guess + (number/guess))/2
        guess = average

        square = guess * guess

        if ((square - number) < .01):
            guess = round(guess, 2)

            if set_flag:
                guess = str(guess)
                guess += 'i'
            return guess
        else:
            count += 1
            if count > 50:
                print("something broke.  sorry!")
                break;

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def prompt_user():
    global set_flag
    user_str = input("What is the number you want to find the approximate square root of?")

    # check if the string is a float if it is - reset string to rounded number
    if isfloat(user_str):
        user_str = round(float(user_str))

    # check if the string is a positive or negative number
    try:
        user_num = int(user_str)
        if user_num < 0:
            set_flag = True
            user_num = user_num * -1

        user_num = int(user_str)

    except ValueError:
        print("That's not an int!")
        user_num = prompt_user()

    return user_num

set_flag = False
user_num = prompt_user()
print(find_sq_root(user_num))
