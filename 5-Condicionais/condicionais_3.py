import sys

valor_1 = int(sys.argv[1])
valor_2 = int(sys.argv[2])

maior = valor_1 if valor_1 > valor_2 else valor_2

print(f"O maior valor é {maior}")
