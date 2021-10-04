n = int(input("Insira o numero para verificar se eh primo: "))
mult = 0

for count in range(2,n):
  if (n % count == 0):
    print("O numero escolhido eh multiplo de " + str(count))
    mult += 1

if(mult == 0):
  print("Eh primo")
else:
  print("Existem " + str(mult) +" numeros multiplos de 2 ate " + str(n))