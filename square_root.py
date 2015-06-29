# script that asks the user for a positive number
# then use Newton's Method to find square root with a maximum error of 0.01.
# You then print out your answer to the user.

#get_num() asks for positive number and validates input
def get_num():
    raw_input_num = input("\nPick a positive number: ")
    while True:
        try:
            input_num = float(raw_input_num)
            return input_num
            break
        except:
            print("\nPlease make sure it is a number and it is positive. ")
            raw_input_num = input("\nPick a positive number: ")
        #print("End of try-except")

def square_root():
    input_num = get_num()
    # x = number you want root of
    # y = guess
    # guess = average = (y, x/y)
    #first you need a guess. HOW? random? half it?
    first_guess = input_num / 2.0
    print("First Guess is {}".format(first_guess))


square_root()
