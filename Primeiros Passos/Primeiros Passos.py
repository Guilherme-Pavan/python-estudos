# Para comentar uma linha em Python eu utilizo  "#". Então tudo que estiver nessa linha vai ser ignorado

"""
Esse é o comentário longo, então  tudo que eu digitar dentro dessa aspas vai ser ignorado

Testando essa parte do comentário

"""

#-------------------------------------------------------

"""
O Python ele é inteligente o suficiente para entender o que cada variável significa, aqui embaixo é caractere, então ele já atribui para a variável
de forma automática
"""

nome = 'Ana Paula' #Ele já reconhece o tipo da variável e já atribui para nome
print(nome)

nome = 23
print(nome)

nome = 25 + 37
print(nome)

# Você consegue colocar várias variáveis na mesma linha, mas precisa colocar o ; para dar sequência

nomeUsuario = "Amanda"; sobreNomeUsuario = "Souza"

print(nomeUsuario + sobreNomeUsuario) #Aqui ele concatena
print(nomeUsuario, sobreNomeUsuario) #Aqui ele separa os nomes

print("Nome: ", nomeUsuario)
print("Sobrenome: ", sobreNomeUsuario)