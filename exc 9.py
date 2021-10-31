'''
exc 9
Solicitar no teclado uma frase com no máximo 40 letras.
Se o tamanho for maior que 40, dar uma mensagem de
entrada inválida e solicitar novamente, se passar, imprimir a
frase na vertical com um tempo em cada letra.
'''
nome = input("Digite uma frase: ")
if len(nome) > 40:
    print("Sua mensagem tem mais de 40 caracteres")
else:
    for nome in nome:
        print(nome)
#for nome in input("Digite seu nome: "): print(nome)
