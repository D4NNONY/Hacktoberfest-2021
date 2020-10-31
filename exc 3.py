'''
exc 3
Receber do teclado uma mensagem e imprimir quantas
letras A, E, I, O, U tem esta mensagem
'''
msg = input('digite uma mensagem qualquer:')
vogais = 0
vogais = vogais + msg.count('A') + msg.count('a')
vogais = vogais + msg.count('E') + msg.count('e')
vogais = vogais + msg.count('I') + msg.count('i')
vogais = vogais + msg.count('O') + msg.count('o')
vogais = vogais + msg.count('U') + msg.count('u')
print('Há {} vogais nesta mensagem'.format(vogais))
