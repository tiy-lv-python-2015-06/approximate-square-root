# script that asks the user for a positive number
# then use Newton's Method to find square root with a maximum error of 0.01.
# You then print out your answer to the user.

#get_num() asks for positive number and validates input
def choose_num():
    while True:
        raw_input_num = input("\nPick a positive number: ")
        try:
            input_num = float(raw_input_num)
            if input_num >= 0:
                return input_num
            else:
                print("\nPlease pick a POSITIVE number")
        except:
            print("\nPlease make sure it is a number and it is positive. ")
            raw_input_num = input("\nPick a positive number: ")
        #print("End of try-except")

def square_root():
    epsilon = 0.01
    picked_num = choose_num()
    counter = 1
    guess = 1
    #test my guess
    test_my_guess = picked_num - (guess * guess)
    print("test_my_guess is {}".format(test_my_guess))
    while test_my_guess > epsilon:
        guess = ((guess) + (picked_num/guess)) / 2
        test_my_guess = (guess * guess) - picked_num
        print("Guess #{} is {}, epsilon is {}".format(counter, guess, test_my_guess))
        counter += 1
    print("The square root of {} is {} ".format(picked_num, guess))

square_root()
