import sys

palavra = sys.argv[1]

primeiras_tres_letras = []
ultima_letra = palavra[-1]

for indice in range(0, 3):
    primeiras_tres_letras.append(palavra[indice])

print("Primeiras três letras:", primeiras_tres_letras, "última letra:", ultima_letra)
