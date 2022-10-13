
while True:
    numero = int(input('Digite um numero para ver sua tabuada '))
    if numero < 0:
        break
   
    for cont in range(1, 11):
        print('-'*40)
        print(f'{numero} X {cont} = {numero*cont}')
print('PROGRAMA ENCERRADO')





    



