'''
exc 5
Criar um algoritmo que entre com uma palavra e
imprima conforme exemplo a seguir:
Exemplo: SONHO
Como a palavra SONHO tem 5 letras a impressão ficaria
assim:
SONHO
SONHO SONHO
SONHO SONHO SONHO
SONHO SONHO SONHO SONHO
SONHO SONHO SONHO SONHO SONHO
Repare que foram impressos 5 vezes na horizontal e 5 na
vertical
'''
word = input('digite a palavra e veja o que acontece: ')
word += ' '
for i in range(len(word)-1):
    print(word* (i+1))
    
input()
