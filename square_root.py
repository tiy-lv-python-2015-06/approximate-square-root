# script that asks the user for a positive number
# and then compute the square root with a maximum error of 0.01.
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
            raw_input_num = input("\nPick a positive number ")
        #print("End of try-except")

        
