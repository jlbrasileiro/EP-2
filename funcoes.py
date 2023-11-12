import random
from unidecode import unidecode
#Filtra as palavras para determinados tamanhos e com letras minusculas
def filtra(palavras,letras):
    palavras_novas = set()

    for palavra in palavras:
        palavra = palavra.strip()
        palavra = palavra.lower()
        palavra_normais = ''.join(i for i in unidecode(palavra)if i.isalpha())

        if len(palavra_normais) == letras:
            palavras_novas.add(palavra_normais)
    return list(palavras_novas)
    
#Mostra se as letras e suas posições estão corretas
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


#Cria um dicionário com as configurações do jogo
def inicializa(palavras, n):
    
    configuracao = {
        'n': n,
        'tentativas': n + 1,
        'especuladas': [],
        'sorteada': random.choice(palavras)
        
    }
    
    while len(configuracao['sorteada']) != n:
        configuracao['sorteada'] = random.choice(palavras)
    return configuracao




