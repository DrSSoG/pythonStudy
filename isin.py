
def sortString(x):
    tab = []
    for char in x:
        tab.append(char)
        print(char)

    tab.sort()
    x = tab
    ans = ''
    for el in x:
        ans += el
    return ans
print(sortString('bdackjoe'))
