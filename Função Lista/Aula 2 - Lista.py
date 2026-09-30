#Imprimindo o valor mínimo e máximo de uma determinada lista.

listaMinMax = [52,10,20,100,50,300,5]

print(min(listaMinMax)) #Mostra o valor mínimo da lista
print(max(listaMinMax)) #Mostra o valor máximo da lista

print("\n\n")
#-----------------------------------------------------------

#Uma lista com números de 1 até 100 parando no valor 10.

listaNumeros1ate10 = [posicao for posicao in range(101) if posicao <= 10]
print(listaNumeros1ate10)

print("\n\n")
#------------------------------------------------------------

#Lista imprimindo de dois em dois.

listaDoisEmDois = list(range(1,101,2))
print(listaDoisEmDois)

print("\n\n")
#------------------------------------------------------------

#Copiando listas.

listaOriginal = ["Lamborghini", "Ferrari", "Cavalo", "Touro"]
listaCopiada = listaOriginal.copy()
print(listaOriginal)
print(listaCopiada)

print("\n\n")
#------------------------------------------------------------

#Unindo listas.

lista1Numeros = [1,2,3]
lista2Letras = ["A", "B", "C"]

#Unindo listas - Join

listaJoin = lista1Numeros + lista2Letras
print(listaJoin)

print("\n\n")
#------------------------------------------------------------

#Outra forma de unir listas.

l1 = ["A1", "B2", "C3"]
l2 = [11,12,13]

for item in l2:
    l1.append(item)

print(l1)
