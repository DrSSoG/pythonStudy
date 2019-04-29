
def iterPower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

def recurPower(base, exp):
    if exp <= 0:
        return 1 
    else:
        return base * recurPower(base, (exp-1))

print('Recursive:', recurPower(2, -1))
print('Iterative:', iterPower(3, 4))
