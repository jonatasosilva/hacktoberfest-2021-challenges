n = int(input('Insira um numero para mostrar a sequencia de Fibonacci: '))

a, b = 0, 1

while a < n:
    print(a, end=' ')
    a, b = b, a+b 