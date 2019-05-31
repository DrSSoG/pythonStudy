top = 300
bottom = 0
step = 20

fahr = bottom
while fahr <= top:
    celsius = 5 * (fahr - 32) / 9
    print('Fahr: ' + str(fahr) + '|' + 'Cels: ' + str(int(celsius)))
    fahr = fahr + 20

