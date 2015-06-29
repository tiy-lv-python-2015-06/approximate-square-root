# script that asks the user for a positive number
# then use Newton's Method to find square root with a maximum error of 0.01.
# You then print out your answer to the user.

#get_num() asks for positive number and validates input
def choose_num():
    raw_input_num = input("\nPick a positive number: ")
    while True:
        try:
            input_num = float(raw_input_num)
            return input_num
        except:
            print("\nPlease make sure it is a number and it is positive. ")
            raw_input_num = input("\nPick a positive number: ")
        #print("End of try-except")

def square_root():
    epsilon = 0.01
    picked_num = choose_num()
    # x = number you want root of
    # y = guess
    # next guess = average of (y, x/y)
    #first you need a guess. just pick the number 1
    # first_guess = picked_num / 2.0
    guess = 1
    #test my guess
    test_my_guess = picked_num - (guess * guess)
    print("test_my_guess is {}".format(test_my_guess))
    while test_my_guess > 0.01:
    #while test_my_guess > 0.1:
        #next guess is = (first_guess + (picked_num/first_guess)/2 )
        guess = ((guess) + (picked_num/guess)) / 2
        test_my_guess = (guess * guess) - picked_num
        print("This Guess is {}, test_my_guess is {}".format(guess, test_my_guess))
    print("The square root of {} is {} ".format(picked_num, guess))

square_root()
