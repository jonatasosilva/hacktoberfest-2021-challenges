n = int(input("Insira o numero para verificar se eh primo: "))
mult = 0

for count in range(2,n):
  if (n % count == 0):
    mult += 1

if(mult == 0):
  print(str(n) + " eh primo")
else:
  print(str(n) + " nao eh primo")