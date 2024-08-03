import colorama
from colorama import Fore, Style

taxas = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suiço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}

# Solicitar a quantidade de dinheiro ao usuário em reais
valor_reais = float(input('Digite o valor em real que você quer converter R$: '))


def calcular_conversao(valor_reais, taxas):
    """
    Calcula a conversão do valor em reais para outras moedas com base nas taxas fornecidas.

    Args:
        valor_reais (float): O valor em reais a ser convertido.
        taxas (dict): Um dicionário contendo as taxas de câmbio.

    Returns:
        dict: Um dicionário com as quantidades convertidas para cada moeda.
    """
    conversoes = {}
    for moeda, taxa in taxas.items():
        quantidade = valor_reais / taxa
        conversoes[moeda] = quantidade
    return conversoes
def exibir_conversoes(conversoes):
    """
    Exibe as conversões calculadas.

    Args:
        conversoes (dict): Um dicionário com as quantidades convertidas para cada moeda.
    """
    print('_____ Conversões: _____')
    for moeda, quantidade in conversoes.items():
        print(f'{Fore.BLUE}{moeda}{Style.RESET_ALL}:{Fore.LIGHTGREEN_EX}{quantidade:.2f}{Style.RESET_ALL}')

# Calcular as conversões:
conversoes = calcular_conversao(valor_reais,taxas)

# Exibir as conversões
exibir_conversoes(conversoes)