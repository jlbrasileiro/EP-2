import random, math
from funcoes import filtra,inidica_posicao,inicializa
from palavras import PALAVRAS





letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# Montando cabeçalho do jogo
print(f"""
         ========================
        |                         |
        | Bem vindos ao jogo termo|
        |                         |
          ===Desing de software===""")




lista_escolhida= filtra(PALAVRAS,letras)
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
          if comparacao[posicao] == 0:
            resultado_parcial += (f'\033[0;32;40m {chute[posicao]} \033[m')
          elif comparacao[posicao] == 1:             
            resultado_parcial += (f'\033[0;33;40m {chute[posicao]} \033[m')
          elif comparacao[posicao] == 2:
            resultado_parcial += (f'\033[0;37;40m {chute[posicao]} \033[m')
      print(resultado_parcial)
      tentativas +=1

      c = comparacao.count(0)

      if c == letras:
         tentativas = dicio_inicial['tentativas']
      else:
         tentativas += 1
  if c == letras and tentativas < dicio_inicial['tentativas']:
     print(f'\033[1;31;40m Uhuu, palavra correta \033[m') 
  elif c != letras and tentativas == dicio_inicial['tentativas']:
     print(f'\033[1;31;40m] Ihhhhh, não conseguiu :( ... A palavra era {resposta_escolhida}')
      

  

  

   




    

    

          


