'''
exc 10
Escrever um programa que receba um nome
-Que conte o número de vogais existentes nele.
-O programa deverá imprimir o número total de
caracteres do nome
-Quantas vogais
- E a respectiva porcentagem das vogais em relação
ao total de caracteres.
'''
nome = input("Digite um nome: ")
a = nome.count('a')
numTotalNome = len(nome)
porcen = (a / numTotalNome) * 100
print("esse nome possui ",numTotalNome, "caracteres")
print("A proporção de vogais do nome é de ", porcen, "%")
