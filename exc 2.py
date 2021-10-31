'''
exc 2
Receber do teclado um nome e imprimir tantas vezes
quantos forem seus caracteres.
'''
name = input('Coloque um nome: \n')
print('-------------')
for _ in range(len(name)):
    print(name)
