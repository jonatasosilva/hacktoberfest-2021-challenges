def fatorial(numero):
    if numero == 0:
        return 1

    return numero * fatorial(numero - 1)


def main():
    numero = int(input())
    print(fatorial(numero))


if __name__ == '__main__':
    main()
