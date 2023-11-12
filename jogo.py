#Importações necessárias
import random, math
from funcoes import filtra,inidica_posicao,inicializa
from palavrass import palavras

# Montando cabeçalho do jogo
print("""
         ========================
        |                         |
        | Bem vindos ao jogo termo|
        |                         |
          ===Desing de software===""")
# Montando cabeçalho de regras
print(f'''Comandos:desisto
      
      Regras: 
      - Você têm 6 tentativas para acertar uma palavra aleatória de 5 letras.
      - A cada tentativa a palavra testada terá suas letras coloridas conforme:
       .\033[0;34;40m {'Azul'} \033[m: a letra está na posição correta;
       .\033[0;33;40m] {'Amarelo'} \033[m: a palavra tem a letra na posição correta;
       .\033[0;37;40m] {'Cinza'}  \033[m: a palavra não tem a letra.
      - Os acentos são ignorados;
      - As palavras podem possuir letras repetidas.

      ''')
#letras é o número de letras da palavra
for i in range(len(palavras)):
   
  letras =  len(palavras[i])
#Escolhendo a lista de palavras 
lista_escolhida= filtra(palavras,letras)
#Escolhendo o dicionário com as configurações do jogo
dicio_inicial = inicializa(lista_escolhida)
#Sorteando a palavra 
resposta_escolhida = dicio_inicial['sorteada']

tentativas = 0
while tentativas < dicio_inicial['tentativas']:
  chute =  input('Tente uma palavra com 5 letras:').lower()
#compara a palavra sorteada com o chute feito
  comparacao = inidica_posicao(dicio_inicial['sorteada'],chute)

  if comparacao == []:
      print('Essa palavra não possui 5 letras, tente novamnete com o número correto')
      tentativas = tentativas
  elif chute == resposta_escolhida:
      print(f'\033[1;31;40m Parabéns! Você acertou a palavra: {resposta_escolhida} \033[m')
      break
  else:
      resultado_parcial = ''
      for posicao in range(len(comparacao)):
          if comparacao[posicao] == 0:
            resultado_parcial += (f'\033[0;34;40m {chute[posicao]} \033[m')
          elif comparacao[posicao] == 1:             
            resultado_parcial += (f'\033[0;33;40m {chute[posicao]} \033[m')
          elif comparacao[posicao] == 2:
            resultado_parcial += (f'\033[0;37;40m {chute[posicao]} \033[m')
      print(resultado_parcial)
      tentativas +=1
#Depois do número máximo de tentativas
if tentativas == dicio_inicial['tentativas']:
   print(f'\033[1;31;40m Ihhhhh, não conseguiu :( ... A palavra era {resposta_escolhida} \033[m')

  

   




    

    

          


