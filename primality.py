
def getNumber():
    return int(input('Give me a number: '))

def checkNumber(number):
    for i in range(1, number):
        if number % i == 0 and number % number == 0:
            return True
        else:
            return False

num = getNumber()
result = checkNumber(num)
print(result)

