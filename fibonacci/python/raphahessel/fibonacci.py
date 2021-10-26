def fibonacci(numero, memo={0: 0, 1: 1}):
    if numero not in memo:
        memo[numero] = fibonacci(numero - 1) + fibonacci(numero - 2)

    return memo[numero]


def main():
    numero = int(input())
    
    for i in range(numero):
        print(fibonacci(i), end=' ')


if __name__ == '__main__':
    main()