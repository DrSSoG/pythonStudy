x = 25
epsilon = 0.01
numberOfGuesses = 0
lowerValue = 1
higherValue = x 
guess = (higherValue + lowerValue) / 2

while abs(guess**2 - x) >= epsilon:
    print('Lower value: ' + str(lowerValue) + ' Higher value: ' + str(higherValue) + ' Guess: ' + str(guess))
    numberOfGuesses += 1
    if guess**2 < x:
        lowerValue = guess
    else:
        higherValue = guess
    guess = (higherValue + lowerValue) / 2 

print('Number of guesses: ' + str(numberOfGuesses))
print(str(guess) + ' is close to square root of ' + str(x))
