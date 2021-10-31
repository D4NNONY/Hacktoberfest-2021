'''
exc 9
Solicitar no teclado uma frase com no máximo 40 letras.
Se o tamanho for maior que 40, dar uma mensagem de
entrada inválida e solicitar novamente, se passar, imprimir a
frase na vertical com um tempo em cada letra.
'''

while True:
      word=input("Escreva uma frase: \n")
      if len(word) > 40:
            print("entrada inválida \n")
            continue
      else:
            for wo in word:
                  print(wo,"\n")
            break