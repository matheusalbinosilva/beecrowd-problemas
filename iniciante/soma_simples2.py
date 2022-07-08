linha_1 = input().split(' ')
linha_2 = input().split(' ')
cod1, numero_pecas1, valor_pecas1 = linha_1
cod2, numero_pecas2, valor_pecas2 = linha_2
soma1 = int(numero_pecas1) * float(valor_pecas1)
soma2 = int(numero_pecas2) * float(valor_pecas2)
total = soma1 + soma2
print('VALOR A PAGAR: R$ {:.2f}'.format(total))

