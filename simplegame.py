def ex1():
    name = input('Please enter your name: ')
    age = int(input('Now tell me your age: '))
    older = 2019 + 100 - age
    msg = ('Nice to meet you ' + name + '. You will turn 100 in year ' + str(older))
    number = int(input('Type a number: '))
    print(number * (msg + '\n'))

def exerciseTwo():
    number = int(input('Give me a number: '))
    if number % 2 == 0:
        print('Even')
    if number % 4 == 0:
        print(' and divisible by 4')
    else:
        print('Odd')
    
    print('==')
    num = int(input('What number to check? '))
    check = int(input('By what to divide it'))
    if num % check == 0:
        print('It divides without remainer')
    else:
        print('It divides with the remainder')
def ex3():
    pass


#FUNCTION CALLS
exerciseTwo()
