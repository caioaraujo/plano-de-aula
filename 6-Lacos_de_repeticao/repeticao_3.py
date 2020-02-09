import sys

numero = int(sys.argv[1])

while numero > 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1
