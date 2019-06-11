def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()

while True:
    n = int(input('Where to end? '))
    if n == 0:
        break
    fib(n)
