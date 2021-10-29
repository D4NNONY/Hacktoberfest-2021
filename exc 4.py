'''
exc 4
Receber um nome no teclado e imprimir quantas letras
"A" tem o nome. 
'''
word = input('digite o nome e nós contamos os "A": ')
count  = word.count('a',0)
count += word.count('A',0)
print('Encontramos um total de ',count,' letras A')
input()
