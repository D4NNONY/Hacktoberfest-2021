'''
exc 7
Receber do teclado a sigla do estado de uma pessoa e
imprimir uma das seguintes mensagens:
Carioca
Paulista
Mineiro
Outros estados
'''

uf = str(input("insira a sigla do seu estado: "))

if (uf == "sp"):
  print("paulista")
elif (uf == "rj"):
  print("carioca")
elif (uf == "mg"):
  print("mineiro")
else:
  print("outros estados")
