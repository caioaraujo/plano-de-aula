import sys

nota_1 = float(sys.argv[1])
nota_2 = float(sys.argv[2])
nota_3 = float(sys.argv[3])

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print("Passou com conceito A")
elif media > 5 and media < 7:
    print("Passou com conceito B")
else:
    print("Reprovado")
