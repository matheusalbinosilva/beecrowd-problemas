id_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())
salario = horas_trabalhadas * valor_hora
print('''NUMBER = {}
SALARY = U$ {:.2f}'''.format(id_funcionario, salario))
