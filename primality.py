''' Simple program checking if input is a primary number'''

# Gets the integer from user
def getNumber():
    return int(input('Give me a number: '))

# Checks the integer given by user
def checkNumber(number):
    if number == 2 or number == 3:
        return True
    else:
        for i in range(2, number-1):
            if number % i != 0:
                return True
            else:
                return False

num = getNumber()
result = checkNumber(num)
print('Result of the check: ' + str(result))


