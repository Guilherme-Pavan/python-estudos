"""
🟢 Exercício 1 — Contagem de 1 a 10

Nível: Fácil

Crie um programa que utilize o for para exibir os números de 1 até 10.

CODIGO:

contador = 1

for contador in range(1,11):
    print(contador)

"""

"""
🟢 Exercício 2 — Tabuada

Nível: Fácil

Crie um programa que solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

CÓDIGO: 

contador = 1
numero = int(input("Digite um número e descubra sua tabuada: "))

for contador in range(1,11):
    multiplicador = numero * contador
    print(numero, " x ", contador, "=", multiplicador)

"""

"""
🟡 Exercício 3 — Soma de números

Nível: Intermediário

Crie um programa que solicite 5 números ao usuário e, ao final, exiba a soma de todos eles.

CÓDIGO: 

soma = 0

for contador in range(1,6):
    numero = int(input("Digite um número: "))
    soma += numero

print(f"A soma dos cincos números é: {soma}")

"""

"""
🟡 Exercício 4 — Identificar números pares e ímpares

Nível: Intermediário

Crie um programa que percorra os números de 1 até 20 e informe se cada número é par ou ímpar.

CÓDIGO: 

for contador in range(1,21):
    if contador % 2 == 0:
        print(contador, " - ", "PAR")
    else:
        print(contador, " - ", "IMPAR")

"""

"""
🔴 Exercício 5 — Média e aprovação dos alunos

Nível: Desafiador

Crie um programa que cadastre 5 alunos, solicitando o nome e a nota de cada um.

for contador in range(1,6):
    aluno = str(input("Digite um aluno: "))
    nota = int(input("Digite sua nota: "))

    if nota >= 7:
        print("Aluno Aprovado")
    elif nota >= 5:
        print("Aluno de Recuperação")
    else:
        print("Aluno Reprovado")

"""







