respostas = 'S'
media = tentativas = soma = maior = menor = 0
while respostas in 'Ss':
    numero = int(input('Digite um numero inteiro :'))
    respostas = str(input('quer continuar ? S / N :')).strip().upper()[0]
    tentativas += 1
    soma += numero
    if numero == 1:
        maior = menor = numero
    else:
        if numero > maior:
            meior = numero
        if numero < menor:
            menor = numero
media = numero / tentativas

print('VOCE DIGITOU {} NUMEROS E A MEDIA FOI {} '.format(tentativas, media))
print('O manor valor foi {} e o maior foi {} .'.format(menor, maior))
