'''
exc 9
Solicitar no teclado uma frase com no máximo 40 letras.
Se o tamanho for maior que 40, dar uma mensagem de
entrada inválida e solicitar novamente, se passar, imprimir a
frase na vertical com um tempo em cada letra.
'''

frase = str(input("insira uma frase com no máximo 40 letras: "))

while len(frase) > 40:
    print(f'entrada inválida!')
    frase = str(input("insira novamente: "))
for letra in frase:
        print(letra)
