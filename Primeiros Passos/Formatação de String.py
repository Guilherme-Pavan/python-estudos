from builtins import len

#----------------------------------------------------------------------------------------

nome = "Luis Guilherme Pavan"
print(nome)
print("Total de Caracteres: " + str(len(nome)))
print(nome[0])
print(nome[0:5])
print(nome[5:15])
print(nome[15:])

#----------------------------------------------------------------------------------------

frase = "CUrSo de LóGICa DE progrAMAçÃo Em PyTHON"
print(frase.upper()) #O upper retorna todas as letras em maiúsculas
print(frase.lower()) #O lower retorna todas as letras em minúsculas

#----------------------------------------------------------------------------------------

notaProva = "Tirei nota cinco na prova"
print(notaProva.replace("cinco", "dez")) #Replace localiza a palavra na variável e substitui para qual você inserir

#----------------------------------------------------------------------------------------

cpf = "123.456.789-10"

cpfPartes = cpf.split(".")
print(cpfPartes)
print(cpfPartes[0])
print(cpfPartes[1])
print(cpfPartes[2])

cpfPartes2 = cpfPartes[2].split("-")
print(cpfPartes2[0])
print(cpfPartes2[1])

print("CPF: " + cpfPartes[0] + cpfPartes[1] + cpfPartes2[0] + cpfPartes2[1])

#----------------------------------------------------------------------------------------



