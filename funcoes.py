import random, math
from palavras import PALAVRAS


def filtra(PALAVRAS,letras):
    palavras_novas = set()

    for palavra in PALAVRAS:
        palavra = palavra.strip()
        palavra = palavra.lower()
        palavra_normais = ''.join(i for i in palavra if i.isalnum())

        if len(palavra_normais) == letras:
            palavras_novas.add(palavra_normais)
    return list(palavras_novas)
    


def inicializa(PALAVRAS):
    configuração = {
        'n': len(PALAVRAS[0]),
        'tentativas':len(PALAVRAS[0])+1,
        'especuladas': [],
        'sorteada': random.choice(PALAVRAS)
        
    }
    return configuração

def inidica_posicao(sorteada,especulada):
    if len(especulada) != len(sorteada):
        return []
    
    lista = []
    for i in range(len(sorteada)):
        if especulada[i] == sorteada[i]:
            lista.append(0)
        elif especulada[i] in sorteada:
            lista.append(1)
        elif especulada[i] not in sorteada:
            lista.append(2)
    
    return lista








