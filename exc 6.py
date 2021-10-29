'''
exc 6
Receber um nome do teclado e imprimí-lo de trás pra
frente.
'''
word = input('digite a palavra e veja o que acontece: ')
word = list(word)
word.reverse()
word = ''.join(word)
print(word)
input()
