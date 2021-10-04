def main():
    n = int(input("Insira o valor de n: "))
    fatorial = 1
    i = 2
    while i <= n:
        fatorial = fatorial*i
        i = i + 1

    print("O fatorial de " + str(n) + " eh : " + str(fatorial))


main()