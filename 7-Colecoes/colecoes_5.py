import sys

item_1 = sys.argv[1]
item_2 = sys.argv[2]
item_3 = sys.argv[3]
item_4 = sys.argv[4]
item_5 = sys.argv[5]

lista_1 = [item_1, item_2, item_3, item_4, item_5]
lista_2 = ["camisa", "bermuda", "sapato"]
lista_1.extend(lista_2)

for item in lista_1:
    print(item)
