'''
Exc 1
Ler nome, sexo e idade. Se sexo for feminino e idade
menor que 25. Imprimir o nome da pessoa e a palavra
ACEITA. Caso contrario imprimir NAO ACEITA.
'''

nome = String(input("insira seu nome: "))
sexo = String(input("insira seu sexo: "))
idade = int(input("insira sua idade: "))

if (sexo == "feminino" and idade < 25):
  print("ACEITA")
else:
  print("NAO ACEITA")
