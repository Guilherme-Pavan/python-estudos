"""
A diferença das listas para tuplas é que não podemos editar os elementos da Tupla, não podemos adicionar elementos, não podemos
remover elementos

"""

tuplaLetras = ("A", "B", "C", "D")
print(tuplaLetras) #Imprimindo a Tupla
print(type(tuplaLetras)) #Imprimindo o tipo da Tupla
print(len(tuplaLetras))  #Tamanho da Tupla
print(tuplaLetras[0]) #Acessando os itens da tupla
print(tuplaLetras[1]) #Acessando os itens da tupla
print(tuplaLetras[-1]) #Acessando o ultimo item da tupla

#----------------------------------------------------------

novaTupla = ("E",) #Cria uma nova tupla
print(novaTupla) #Imprime a tupla
print(type(novaTupla)) #Mostra o tipo do dado

tuplaLetras += novaTupla #Unindo a tupla

print("\n") #Quebra de linha
print(tuplaLetras) #Imprimindo a tupla

#----------------------------------------------------------

tuplaNumeros = (1,2,3,4,5,6,7)
listaNumeros = list(tuplaNumeros) #Convertendo tupla em lista
listaNumeros.remove(4) #Removendo o item 4 da lista
tuplaNumeros  = tuple(listaNumeros) #Convertendo lista em tupla
print("\n")
print(tuplaNumeros)
print("\n")
#----------------------------------------------------------

#Imprimindo itens da Tupla

tuplaFrutas = ("Banana", "Abacaxi", "Laranja", "Maçã")

for item in tuplaFrutas:
    print(item)



