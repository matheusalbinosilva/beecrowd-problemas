valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite o segundo valor :'))
opcao = 0
while opcao != 5:
    print('''MENU 
    [1] SOMAR
    [2] MULTIPLICAR 
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        soma = (valor1 + valor2)
        print(soma)
    elif opcao == 2:
        print(valor1 * valor2)
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(maior)
    elif opcao == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite o segundo valor :'))
    elif opcao == 5:
        print('FIM DO PROGRAMA ')
    else:
        print('Opção invalida, digite novamente: ')

