print('This is gona be a repeat of everything Python\'y')

#declaring variables I don't remember if this is a comment 
numberOne = 5
numberTwo = 8
name = 'Bourbon'
surname = 'Whiskey'

#using all possible operators and achieving all outcomes=============================================
print('=====[OPERATORS AND THEIR USE]===========')
print('This is a sum: ', numberOne, ' + ', numberTwo, ' = ', numberOne + numberTwo)
print('This is a differnce: ', numberOne, ' - ', numberTwo, ' = ', numberOne - numberTwo)
print('This is a multiplication: ', numberOne, ' * ', numberTwo, ' = ', numberOne * numberTwo)
print('This is a division: ', numberOne, ' / ', numberTwo, ' = ', numberOne / numberTwo)
print('This is a rest of division: ', numberOne, ' % ', numberTwo, ' = ', numberOne % numberTwo)

#loops repetition====================================================================================
print('=====[LOOPS]===========')
for i in range(0, 5):
    print('Number ', i )

print('================')

counter = 0
while(counter < 3):
    print('Count ', counter)
    counter += 1

#conditions==========================================================================================
print('======[CONDITIONS]==========')
if(name == 'Bourbon'):
    print('Hello there my love')
elif(name == 'Vodka'):
    print('What\'s up bitch?')
else:
    print('I don\'t know you')

print('================')

if(name == 'Bourbon' and surname == 'Whiskey'):
    print('Me love you long time')

#functions===========================================================================================
print('======[FUNCTIONS]==========')
def funkcjaLicz(numberOne, numberTwo):
    print('Expression equals: ', numberOne + numberTwo * 5)
    answer = input('Is this correct y/n? ')
    if(answer == 'y'):
        print('Correct')
    elif(answer == 'n'):
        print('Incorrect')
    else:
        print('You\'ve put the wrong symbol in')

funkcjaLicz(numberOne, numberTwo)

#lists===============================================================================================
print('======[LISTS/TUPLES/DICTIONARIES]==========')




#classes/methods=====================================================================================
print('======[CLASSES]==========')
class Counters:
    def addition(no1, no2):
        return no1 + no2
    surname = 'Nowak'

print(Counters.addition(numberOne, numberTwo))
print(Counters.surname)




