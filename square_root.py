while True:
    try:
        your_number = int(input("Please enter a Positive Number ")) #This is where we get a Number
    except ValueError:
        print("Sorry that is not a valid entry")
        continue
    else:
        break
guess = 1
epsilon = 0.001
counter = 0

while True:
    how_far_away = abs((guess * guess) - your_number) #This is to test the number
    if (how_far_away) <= epsilon:
        print(round(guess, 2))
        break
    else:
        guess = (guess + your_number/guess) / 2   #This is the new guess
        counter = counter + 1  #Counter for number of passes
        print(counter, (round(guess, 2)))
