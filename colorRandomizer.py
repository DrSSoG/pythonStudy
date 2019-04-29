import random
print('Color generator in RGB system')
isRunning = True

while isRunning:
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    
    rgbArray = [red, green, blue]
    colorHueLow = [abs(red - 25), abs(green - 25), abs(blue - 25)]
    colorHueHigh = [red + 25, green + 25, blue + 25]
    
    print(colorHueLow)
    print(rgbArray)
    print(colorHueHigh)
 
    prompt = input('Randomize again?')
    if(prompt == 'y'):
        isRunning = True
    else:
        isRunning = False
