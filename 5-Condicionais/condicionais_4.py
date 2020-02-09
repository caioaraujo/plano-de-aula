import sys

valor_1 = int(sys.argv[1])
valor_2 = int(sys.argv[2])

sao_divisiveis = valor_1 % valor_2 == 0

if sao_divisiveis is True:
    print("São divisíveis")
else:
    print("Não são divisíveis")
