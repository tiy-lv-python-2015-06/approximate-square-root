your_number = int(input("Please enter a Positive Number "))

guess = 1
epsilon = 0.001
counter = 0

while True:
    how_far_away = abs((guess * guess) - your_number)
    if (how_far_away) <= epsilon:
        print(round(guess, 2))
        break
    else:
        guess = (guess + your_number/guess) / 2
        counter = counter + 1
        print(counter, (round(guess, 2)))
