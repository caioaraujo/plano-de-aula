import sys

valor_1 = int(sys.argv[1])
valor_2 = int(sys.argv[2])
valor_3 = int(sys.argv[3])
valor_4 = int(sys.argv[4])
valor_5 = int(sys.argv[5])

valores = (valor_1, valor_2, valor_3, valor_4, valor_5)

dicionario = {"pares": [], "impares": []}

for valor in valores:
    if valor % 2 == 0:
        dicionario["pares"].append(valor)
    else:
        dicionario["impares"].append(valor)

print(dicionario)
