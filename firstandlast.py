''' A program that takes a list of numbers and returns 1st and n-th element'''


def getFirstAndLast(numbers):
    newTable = [numbers[0], numbers[len(numbers)-1]]
    print(newTable)
    return newTable

numbers = [5, 10, 15, 20, 25]
getFirstAndLast(numbers)

