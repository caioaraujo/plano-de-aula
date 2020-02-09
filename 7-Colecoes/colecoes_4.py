import sys

item_1 = sys.argv[1]
item_2 = sys.argv[2]
item_3 = sys.argv[3]
item_4 = sys.argv[4]
item_5 = sys.argv[5]

lista = [item_1, item_2, item_3, item_4, item_5]
lista_ordenada = sorted(lista)

for item in lista_ordenada:
    print(item)
