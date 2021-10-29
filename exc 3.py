'''
exc 3
Receber do teclado uma mensagem e imprimir quantas
letras A, E, I, O, U tem esta mensagem
'''
word = input("digite a palavra e nós contamos as vogais: ")
count  = word.count('a',0)
count += word.count('A',0)
count += word.count('e',0)
count += word.count('E',0)
count += word.count('i',0)
count += word.count('I',0)
count += word.count('o',0)
count += word.count('O',0)
count += word.count('u',0)
count += word.count('U',0)
print('Encontramos um total de ',count,' vogais')
input()
