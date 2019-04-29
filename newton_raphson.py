epsilon = 0.01
y = float(input('What number to find square root of? ')) 
guess = y/2.0
numGuesses = 0

while abs(guess**2-y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y) / (2 * guess))

print('Number of guesses: ' + str(numGuesses))
print('Square root of ' + str(y) + ' is aprox ' + str(guess))
