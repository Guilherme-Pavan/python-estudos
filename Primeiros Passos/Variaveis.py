nota1 = nota2 = nota3 = nota4 = media = 0
aluno = "Allan Pires"

print(aluno)

nota1 = 9
print(nota1)

aluno = input("Digite o nome do Aluno: ")
nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a terceira nota: ")
nota4 = input("Digite a quarta nota: ")

media = (float(nota1) + (float(nota2))+ (float(nota3)) + (float(nota4))) / 4

print("Aluno: ", aluno)
print("A média das nota é: ", media)