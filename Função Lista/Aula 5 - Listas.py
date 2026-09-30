listaLetras = ["A", "C", "E", "D", "F", "B"]
print(listaLetras)
listaLetras.sort() #Sort - Ordenando de A a Z
print(listaLetras)

listaLetras.sort(reverse=True) #Ordenando de Z a A
print(listaLetras)

print("\n\n")
#------------------------------------------------------------

listaNumeros = [4, 9, 5, 20, 16, 14, 12]
print(listaNumeros)
listaNumeros.sort()
print(listaNumeros)

listaNumeros.sort(reverse=True)
print(listaNumeros)

print("\n\n")
#------------------------------------------------------------

listaMaiMin = ["Sofá", "tv", "carro", "Casa", "Armario"]
listaMaiMin.sort()
print(listaMaiMin)

listaMaiMin.sort(key=str.lower)
print(listaMaiMin)


