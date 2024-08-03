# 3. Escreva um script que pergunta ao usuário se ele deseja converter
# uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
# cada opção, crie uma função.
# Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
# desejada, onde esse menu chama a função de conversão correta.


def celsius_para_fahrenheit(temperatura):
    return (temperatura * 1.8) + 32


def fahrenheit_para_celsius(temperatura):
    return (temperatura - 32) / 1.8


def menu():
    print("=-= Conversor de temperatura =-=\n")
    while True:

        try:
            temperatura = float(input("Digite a temperatura para conversão\n\n-> "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite uma temperatura válida..\n")

    print("\nEscolha um opção de conversão: \n")
    opcao = input(
        "[F] Fahrenheit para Celsius\n[C] Celsius para Fahrenheit\n\n--> "
    ).upper()

    while opcao not in ["C", "F"]:
        print("Opção Inválida! Selecione uma das opções abaixo: ")
        opcao = input("\n[F] °F para °C\n[C] °C para °F\n\n--> ").upper()

    if opcao == "C":
        resultado = celsius_para_fahrenheit(temperatura)
        print(f"{temperatura}°C são {resultado:.2f}°F")
    else:
        resultado = fahrenheit_para_celsius(temperatura)
        print(f"{temperatura}°F são {resultado:.2f}°C")


menu()
