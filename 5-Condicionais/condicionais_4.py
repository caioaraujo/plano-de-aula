import sys

valor_1 = sys.argv[1]
valor_2 = sys.argv[2]
valor_3 = sys.argv[3]

if valor_1 == "True":
    print("O primeiro valor é verdadeiro")
else:
    print("O primeiro valor é falso")

if valor_2 == "False":
    print("O segundo valor é falso")
else:
    print("O segundo valor é verdadeiro")

if valor_3 != "False":
    print("O terceiro valor é verdadeiro")
else:
    print("O terceiro valor é falso")
