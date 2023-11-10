import palavras
import random, math
from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.RED + 'Texto em vermelho')




letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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





# Montando cabeçalho do jogo
print(f"""
         ========================
        |                         |
        | Bem vindos ao jogo termo|
        |                         |
          ===Desing de software===""")



    

lista_escolhida= filtra(palavras,letras)
dicio_inicial = inicializa(lista_escolhida)
resposta_escolhida = dicio_inicial['sorteada']

tentativas = 0
while tentativas < dicio_inicial['tentativas']:
  chute =  input(f'Tente uma palavra com 5 letras')
  comparacao = inidica_posicao(dicio_inicial['sorteada'],chute)

  if comparacao == []:
      print(f'Essa palavra não possui 5 letras , tente de novo com uma nova palavra com 5 letras')
      tentativas = tentativas
  if chute not in resposta_escolhida:
    print(f'Palavra desconhecida')
  else:
      resultado_parcial = ''
      for posicao in range(len(comparacao)):
          
  

   




    

    

          


