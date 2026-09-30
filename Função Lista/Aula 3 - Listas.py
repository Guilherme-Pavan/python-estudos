lista1 = ["A", "B", "C"]
lista2 = ["D", "E", "F"]

lista1.extend(lista2) #Com extend conseguimos unir duas listas
print(lista1)

lista1.remove("E") #Removendo a letra E da lista
print(lista1)

lista1.pop(2) #Removendo com o POP o segundo elemento da lista
print(lista1)

lista1.pop() #Removendo o último elemento da lista
print(lista1)

#Removendo o primeiro elemento da lista
del lista1[0]
print(lista1)

lista1.clear() #Removendo todos os elementos da lista
print(lista1)

lista1.append("Maçã") #Adicionando itens dentro da lista
print(lista1)

lista1.insert(1, "Goiaba") #Adicionando um item na segunda posição da lista
print(lista1)

lista1.insert(1, "Laranja") #Adicionando um item na segunda posição da lista
print(lista1)

if "Laranja" in lista1:
    print("Sim, a Laranja exista na lista!")
else:
    print("Não encontramos a Fruta!")

lista1[2] = "Banana"
print(lista1)

lista1[1:3] = ["A", "B"]
print(lista1)