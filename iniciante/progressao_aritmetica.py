print('Gerador de PA ')
print('-=' * 8)
primeiro_termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao da PA:'))
termo = primeiro_termo
contador = 1
calculo = 0
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
