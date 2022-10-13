print('-'* 30)
print('      CADASTRE UMA PESSOA          ')
print('-'* 30)
while True:
    idade = int(input('Digite sua idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M / F]:')).strip().upper()[0]
        print(sexo)
   
        