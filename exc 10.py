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

#Implementação

countVogals = 0
characters = input("Introduza o caracter/palavra: ")
backup = []
for character in characters:
    if character == "a" or character == "e" or character == "i" or character == "o" or character =="u":
        if len(backup) == 0:
            backup.append(character)
            countVogals += 1
        else:
            try:
                if backup.index(character) >= 0:
                    pass
            except:
                backup.append(character)
                countVogals += 1
percent = countVogals * len(characters) / 100

# resultado 

print("Numero de vogais existentes ->",countVogals,"->",backup)
print()
print("Total de caracteres existentes ->",len(characters),"->",characters.split())
print()
print("Porcentagem das vogais em relação ao total de caracteres ->", percent)
