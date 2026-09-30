listaNomes = ["Allan", "Bruna", "Simone", "Carla"]

#Imprimindo os itens de uma lista
for posicao in listaNomes:
    print(posicao)

print("\n\n")

#Exemplo com impressão com for 2
[print(item) for item in listaNomes]

print("\n\n")

#Imprimindo uma lista utilizando a função While(Enquanto)

contador = 0
while contador < len(listaNomes): #len() - retorna a quantidade de elementos que existe na lista.
    print(listaNomes[contador])
    contador = contador + 1

print("\n\n")

listaNomesC = []

for item in listaNomes:
    if "a" in item:
        listaNomesC.append(item) #Adiciona o item
print(listaNomesC)

print("\n\n")

listaMaiuscula = [item.upper() for item in listaNomes] #Deixa tudo com a letra maiúscula - upper
print(listaNomes)
print(listaMaiuscula)

listaMinuscula = [item.lower() for item in listaNomes] #Deixa tudo com a letra minúscula - lower
print(listaNomes)
print(listaMinuscula)



