"""
Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício
"""
#importa a biblioteca random
import random

#define uma lista de palavras
palavras = ["gato", "cachorro", "pássaro",
            "elefante", "girafa", "macaco",
            "leão", "tigre", "cobra", "peixe"
            ]

def selecao_palavra():
    """
    usa a biblioteca random para escolher uma palavra aleatória 
    e cria uma máscara do tamanho adequado usando compreensão de lista
    """
    escolhida = random.choice(palavras)

    espacos = ['_' for letra in escolhida]
    return escolhida, espacos

def verificar_letra(letra, escolhida, espacos):
    """
    verifica se a entrada do usuário tem correspondência com a palavra selecionada da lista
    """
    acertou = False
    for i in range(len(escolhida)):
        if escolhida[i] == letra:
            espacos[i] = letra
            acertou = True
    return acertou

#define o jogo 
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
        
        #não adiciona letra repetida só novas letras
        if letra in letras_usadas:
            print('Você já digitou essa letra!')
        else:
            letras_usadas.append(letra)
            if verificar_letra(letra, forca, espacos):
                print('Letra correta!')
            #atualiza número de tentativas
            else:
                print('Errou!')
                tentativas -= 1
    
    #para o loop se a palavra está completa
    if '_' not in espacos:
        print(f'Parabéns, você descobriu! A palavra é {forca}')
    else:
        print(f'Não foi dessa vez! A palavra era {forca}')


#inicia instrução
print('Vamos jogar forca?')
jogo_forca()
