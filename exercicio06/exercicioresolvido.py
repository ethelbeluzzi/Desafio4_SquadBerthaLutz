#importa a biblioteca random
import random

def selecao_palavra():
    """
    usa a biblioteca random para escolher uma palavra aleatória 
    num arquivo externo 
    e cria uma máscara do tamanho adequado usando compreensão de lista

    retorna:
        uma tupla contendo a palavra e a máscara
    """
    with open("exercicio06/palavras.txt", 'r') as arquivo:
       palavras = [palavra.strip() for linha in arquivo for palavra in linha.split()]

    escolhida = random.choice(palavras)

    espacos = ['_' for letra in escolhida]
    return escolhida, espacos

def verificar_letra(letra, escolhida, espacos):
    """
    verifica se a entrada do usuário tem correspondência com a palavra selecionada da lista
    retorna:
        True para acerto ou False para erro
    """
    acertou = False
    for i in range(len(escolhida)):
        if escolhida[i] == letra:
            espacos[i] = letra
            acertou = True
    return acertou

def jogo_forca():
    """
    define a dinâmica do jogo invocando as funções selecao_palavra e verificar_letra
    """
    forca, espacos = selecao_palavra()
    tentativas = 6
    letras_usadas = []

    # desempacota e imprime a máscara da palavra escolhida enquanto o houver tentativas
    while '_' in espacos and tentativas > 0:
        print('Palavra:', *espacos)
        print(f'Tentativas restantes: {tentativas}')
        letra = input('Digite uma letra: ').lower()

        #não adiciona letra repetida só novas letras e não aceita int ou float
        if letra in letras_usadas:
            print('====== Você já digitou essa letra! ====== \n')
        elif len(letra) > 1:
            print('====== Você digitou mais de uma letra ====== \n')
        elif letra.isdigit():
            print(f'====== {letra} não é uma letra! ====== \n')
        else:
            letras_usadas.append(letra)
            if verificar_letra(letra, forca, espacos):
                print('\nLetra correta!\n')
            #atualiza número de tentativas
            else:
                print('\nErrou!\n')
                tentativas -= 1
    
    #para o loop se a palavra está completa
    if '_' not in espacos:
        print(f'Parabéns, você descobriu! A palavra é {forca}')
    else:
        print(f'Não foi dessa vez! A palavra era {forca}')


#inicia instrução
print('===== Vamos jogar forca? =====')
jogo_forca()