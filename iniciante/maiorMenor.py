n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
maior = menor = n1
if n2 > n1:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < n1:
    menor = n2
if n3 < menor:
    menor = n3

print(f'O maior mumero é {maior}, o menor numero {menor}' )

