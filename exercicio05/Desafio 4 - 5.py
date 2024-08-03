# Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.

def contar_vogais(texto):

    conjunto_vogais = 'aeiouAEIOU'
    total_vogais = 0

    for simbolo in texto:
        if simbolo in conjunto_vogais:
            total_vogais += 1

    return total_vogais


frase_inserida = input("Por favor, insira uma frase: ")

numero_vogais = contar_vogais(frase_inserida)

print(f"A frase contém {numero_vogais} vogais.")