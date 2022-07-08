nome = str(input())
salario = float(input())
total_vendas = float(input())
comissao = total_vendas * 15 / 100
salario_bonus = comissao + salario
print('TOTAL = R$ {.2f}'.format(salario_bonus))


