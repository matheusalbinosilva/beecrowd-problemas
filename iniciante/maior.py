a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
maior_ab = int((a + b + abs(a - b)) / 2)
if c > maior_ab:
    print('{} eh o maior'.format(c))
else:
    print('{} eh o maior'.format(maior_ab))
