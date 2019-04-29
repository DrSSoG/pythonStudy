def gcdInter(a, b):
    if a > b:
        for i in range(b, 0, -1):
            if a % i == 0 and b % i == 0:
                return i
    elif a < b:
        for i in range(a, 0, -1):
            if a % i == 0 and b % i == 0:
                return i

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

print(gcdInter(2,12))
print(gcdInter(6,12))
print(gcdInter(3,12))
print(gcdInter(17,12))
print('===================')
print(gcdRecur(2,12))
print(gcdRecur(6,12))
print(gcdRecur(3,12))
print(gcdRecur(17,12))
