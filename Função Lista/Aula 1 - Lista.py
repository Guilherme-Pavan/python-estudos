listaNome = ["Amanda", "Clarisse", "Roger"]

print(listaNome) #Imprimindo os valores da lista - Amanda, Clarisse e Roger
print(len(listaNome)) #Eu consigo saber o tamanho da lista utilizando o len()

#-------------------------------------------------------------------------------

print("\n")

lista1 = ["A", "B", "C"]
lista2 = [1,2,3,4]
lista3 = [True, False, False]
lista4 = ["Roberta", 34, False]

print(lista1)
print(lista2)
print(lista3)
print(lista4)

#-------------------------------------------------------------------------------

print("\n")

#Posição       0       1      2    3        4
listaTeste = ["A", "Banana", "C", "D", "Elefante", "P"]

print(listaTeste[0]) #Imprimindo a posição 0 da listaTeste - Resultado vai ser a letra A.
print(listaTeste[1]) #Imprimindo a posição 1 da listaTeste - Resultado vai ser a palavra Banana.
print(listaTeste[2]) #Imprimindo a posição 2 da listaTeste - Resultado vai ser a letra C.
print(listaTeste[3]) #Imprimindo a posição 3 da listaTeste - Resultado vai ser a letra D.
print(listaTeste[4]) #Imprimindo a posição 4 da listaTeste - Resultado vai ser a palavra Elefante.

print(listaTeste[-1]) #Imprime o último item da listaTeste.
print(listaTeste[1:3]) #Escolhi dois itens da lista e imprimi utilizando o print.
print(listaTeste[:3]) #Imprime os três primeiros itens da listaTeste.
print(listaTeste[2:]) #Imprime a partir do da posição 2 da lista em diante.
print(listaTeste[::2]) #Aqui você imprime de dois em dois - Resultado: ['A', 'C', 'Elefante'] - Posição 0, Posição 2 e Posição 4.
print(listaTeste[::-1]) #Imprimindo a lista de trás para frente. Resultado: ['P', 'Elefante', 'D', 'C', 'Banana', 'A']. 


