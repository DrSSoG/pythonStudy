def printMove(fr, to):
    print('Moving from ' + str(fr) + ' to ' + str(to))

def towers(numOfDiscs, fr, to, spare):
    if numOfDiscs == 1:
        printMove(fr, to)
    else:
        towers(numOfDiscs - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(numOfDiscs - 1, spare, to, fr)

while True:
    ask = int(input('Number of discs'))
    towers(ask, 'LEFT', 'MIDDLE', 'RIGHT')
    
