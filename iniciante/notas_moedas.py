


N = int(input())
n100 = n50 = n20 = n10 = n5 = n2 = n1 = resto = 0
while True:
    if N >= 100:
        n100 = N / 100
        resto = N % 100
    else:
        resto = N
    if resto >= 50:
        n50 = resto / 50
        resto = resto % 50
    if resto >= 20:
        n20 = resto / 20
        resto = resto % 20
    if resto >= 10:
        n10 = resto / 10
        resto = resto % 10
    if resto >= 5:
        n5 = resto / 5
        resto = resto % 5
    if resto >= 2:
        n2 = resto / 2
        resto = resto % 2
    if resto >= 1:
        n1 = resto
        
    break
    
print('{}'.format(N))   
print('{} nota(s) de R$ 100,00'.format(n100.__floor__())) 
print('{} nota(s) de R$ 50,00'.format(n50.__floor__()))  
print('{} nota(s) de R$ 20,00'.format(n20.__floor__()))
print('{} nota(s) de R$ 10,00'.format(n10.__floor__())) 
print('{} nota(s) de R$ 5,00'.format(n5.__floor__()))
print('{} nota(s) de R$ 2,00'.format(n2.__floor__())) 
print('{} nota(s) de R$ 1,00'.format(n1.__floor__()))
