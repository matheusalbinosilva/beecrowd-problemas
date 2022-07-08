nome = str(input())
salario = float(input())
vendas = float(input())
comissao = vendas * 15 / 100
total = salario + comissao
print('TOTAL = {:.2f}'.format(total))

