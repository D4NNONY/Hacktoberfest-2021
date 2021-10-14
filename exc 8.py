'''
exc 8
Entrar com um nome e imprimir o nome somente se a
primeira letra do nome for “a” (maiúscula ou minúscula).
'''
nome = str(input("insira um nome: "))

if (nome[0] == "a" or nome[0] == "A"):
  print(nome)
