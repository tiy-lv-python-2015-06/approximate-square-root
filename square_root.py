epsilon = .01
while True:
    user_root = input("Please enter a number, or [E]xit\n")
    if user_root.lower() == 'e' or user_root == 'exit':
        break
    try:
        user_root = float(user_root)
    except:
        print('Please enter a valid number')
        continue
    if user_root == 0:
        print('The Square root of 0 is 0')
        continue
    if user_root < 0:
        is_negative = '-'
        is_i = 'i'
        user_root = -1 * user_root
    else:
        is_negative = ''
        is_i = ''
    count = 1
    guess = 1
    while True:
        guess = .5 * (guess + (user_root / guess))
        if (guess * guess) - user_root <= epsilon:
            print('The Square root of {}{} is {}{}'.format(is_negative, user_root, round(guess, len(str(epsilon)) - 2), is_i))
            break
        else:
            count += 1
            print('on try {} the square root of {}{} is {}{}'.format(count, is_negative, user_root, round(guess, len(str(epsilon)) - 2), is_i))
