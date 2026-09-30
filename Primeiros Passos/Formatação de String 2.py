
"""

                                                                                                FORMATAÇÃO DE STRINGS - PARTE 2

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

palavraComEspaco = "           Curso de Python           "
print(palavraComEspaco)
print(palavraComEspaco.strip()) #Remove os espaços

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

gostoPorFruta = "Eu gosto de Laranja"
print("Laranja" in gostoPorFruta) #Aqui ele mostra se a palavra "Laranja" se encontra presente na variável "gostoPorFruta", então ele vai retornar verdadeiro ou falso (True or False).

resultado = gostoPorFruta.find("o") #Aqui ele vai buscar a posição que está cada letra da varivável. Nesse caso, está a letra "o" ele vai retornar 4. E-0 / U-1 / ... 2 / G - 3 / O - 4 - Essa é a lógica.
print(resultado)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ganhadorCopa = "O Brasil ganhou a Copa do Mundo"

campeao = "Alemanha" not in ganhadorCopa #Not in (Não está). Aqui quer dizer: A Alemanha não está na variável ganhadorCopa? Vai retornar True, porque ele não está na variável.
print(campeao)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

aluna = "Rebeca Martins"
nota1 = 9.596
nota2 = 6
media = (nota1 + nota2)/2

print("Aluna: " + aluna + " - Media: " + str(media))

print(f"Aluna: {aluna} - Média: {media:.2f}") #Ele diminui as casa decimais. 

ajusteTexto = "Aluna: {} - Média: {}"
print(ajusteTexto.format(aluna, media))