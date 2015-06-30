guess = 1
total = 0
number = 0
iteration = 0
number = input("Enter a positive number: ")
if int(number) < 0:
    print("Error, you entered a negative number!")
else:
    number = int(number)
    while True:
        iteration += 1
        print("This is iteration number {} of the loop.".format(iteration))
        print("The current guess is {}.".format(guess))
        temp = guess * guess - number
        if abs(temp) <= 0.01:
            print("The square root of {} is {}.".format(number, guess))
            break
        else:
            guess = (guess + (number / guess)) / 2
