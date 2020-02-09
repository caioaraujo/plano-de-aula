import sys

numero = int(sys.argv[1])

lista = []

while numero > 0:
    if numero % 2 == 0:
        lista.append(numero)
    numero -= 1

for item in lista:
    print(item)
