sex = input("Sex? (m/f): ")
weight = int(input("Weight[kg]: "))
height = int(input("Height[cm]: "))
age = int(input("Age: "))

if sex == 'm':
    bmr = 66.5 + (13.7*weight) + (5*height) - (6.8*age)
elif sex == 'f':
    bmr = 655 + (9.6*weight) + (1.85*height) - (4.7*age)
else:
    print('Wrong input')

print('Which fits you best?')
print("""No physical activity, sitting or laying [1]
        Seated job, low physical activity [2]
        Not a physical job, training 2 times a week [3]
        Light physical work, training 3-4 times a week [4]
        Physical work, training 5 times a week [5]
        Hard physical work, training every day [6]""")

lifestyle = input("Value fitting yours: ")
if lifestyle == 1:
    modifier = 1.0
elif lifestyle == 2:
    modifier = 1.2
elif lifestyle == 3:
    modifier = 1.4
elif lifestyle == 4:
    modifier = 1.6
elif lifestyle == 5:
    modifier = 1.8
elif lifestyle == 6:
    modifier = 2.0
else:
     print('Wrong value')

totalburned = bmr * modifier
print(totalburned + 'kcal will not cause a significant change in your body')

print('========')
print('''Endomorph [1]
        Mesomorph [2]
        Ectomorph [3]''')

bodyType = input('Choose the proper value again')
if bodyType == 1:
    bodyTypeModifier = 0.1
    reductionModifier = 0.2
elif bodyType == 2:
    bodyTypeModifier = 0.15
    reductionModifier = 0.15
elif bodyType == 3:
    bodyTypeModifier = 0.2
    reductionModifier = 0.1
else:
    print('Wrong value')

finalResult = totalburned + (bodyTypeModifier * totalburned)
reductionResult = totalburned - (reductionResult * totalburned)

print('Keep weight: ' + str(finalResult) + 'kcal')
print('Lose weight: ' + str(reductionResult) + 'kcal')
