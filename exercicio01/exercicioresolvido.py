# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#Definir as funções
def soma_tres_numeros(a, b, c):
    return a + b + c

def pedir_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

# Pedir ao usuário para inserir três números e garantir que sejam válidos
numero1 = pedir_numero("Digite o primeiro número: ")
numero2 = pedir_numero("Digite o segundo número: ")
numero3 = pedir_numero("Digite o terceiro número: ")

# Calcular a soma dos três números
resultado = soma_tres_numeros(numero1, numero2, numero3)

# Imprimir o resultado
print("A soma dos três números é:", resultado)
