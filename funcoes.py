import random, math
from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.RED + 'Texto em vermelho')





def filtra(palavras,letras):
    palavras_novas = set()

    for palavra in palavras:
        palavra = palavra.strip()
        palavra = palavra.lower()
        palavra_normais = ''.join(i for i in palavra if i.isalnum())

        if len(palavra_normais) == letras:
            palavras_novas.add(palavra_normais)
    return list(palavras_novas)
    


def inicializa(palavras):
    configuração = {
        'n': len(palavras[0]),
        'tentativas':len(palavras[0])+1,
        'especuladas': [],
        'sorteada': random.choice(palavras)
        
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

cores = {
    'amarelo': '\033[93m',
    'azul': '\033[94m',,
    'cinza': '\033[90m'
  
}








