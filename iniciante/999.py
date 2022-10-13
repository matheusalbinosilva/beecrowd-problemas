numero = tentativas = soma = 0
numero = int(input('Digite 999 para parar o programa: '))

while numero != 999:
    tentativas += 1
    soma += numero
    numero = int(input('Digite 999 para parar o programa: '))

print('ACABOU, VOCE DIGITOU {} VEZES, E A SOMA DELES É {} '.format(tentativas, soma))
