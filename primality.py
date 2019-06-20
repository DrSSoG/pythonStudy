
def getNumber():
    return int(input('Give me a number: '))

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
print(result)

