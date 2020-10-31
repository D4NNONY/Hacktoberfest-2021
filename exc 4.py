'''
exc 4
Receber um nome no teclado e imprimir quantas letras
"A" tem o nome. 
'''
nome = input('digite um nome qualquer:')
n = nome.count('A') + nome.count('a')
print(nome+' tem {} letras A'.format(n))
