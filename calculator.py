print('Welcome to the C.A.L.C.U.L.A.T.O.R.')
while True:
    numberOne = int(input('Insert the 1st number: '))
    numberTwo = int(input('Insert the 2nd number: '))
    operator = input('Specify the operator: ')
    if(operator == '+' or operator == 'add'):
        equals = numberOne + numberTwo
        print(numberOne, ' + ', numberTwo, ' = ', equals)
    elif(operator == '-' or operator == 'subtract'):
        equals = numberOne - numberTwo
        print(equals)
    elif(operator == '*' or operator == 'multiply'):
        equals = numberOne * numberTwo
        print(equals)
    elif(operator == '/' or operator == 'divide'):
        if(numberTwo == 0):
            print('You cant\'t divide by 0')
        else:
            equals = numberOne / numberTwo
            print(equals)
    elif(operator == '**' or operator == 'exponantiate'):
        print(numberOne ** numberTwo)
    elif(operator == 'q' or operator == 'quit'):
        break
    else:
        print('Incorrect sign of operator')
    print('========================================')

    decision = input('Would you like to save to memory? y/n')
    if(decision == 'y'):
        print('Saved!')
    elif(decision == 'n'):
        continue
    else:
        print('Incorrect sign')
