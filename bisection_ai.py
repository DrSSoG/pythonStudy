print('Please think of a number between 0(inclusive) and 100 (not inclusive')
high = 100
low = 0
guess = int((high+low)/2)
gameOver = False
counter = 0

while not gameOver:
    print('Is your number ' + str(guess) + '?')
    hint = input('Enter \'h\' to idicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to idicate that i got the answer right. \n Hint: ')
    
    if (hint == 'h'):
        high  = guess
    elif (hint == 'l'):
        low = guess
    elif(hint == 'c'):
        gameOver = True
        break
    else:
        print('Incorrect input. Retry...')
        continue

    guess = int((high+low)/2)
    counter += 1

print('Game over! Your secret number was: ' + str(guess))
print('It took me ' + str(counter) + ' guesses...')
