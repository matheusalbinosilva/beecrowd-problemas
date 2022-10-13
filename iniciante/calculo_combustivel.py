horas = int(input())
velocidade_media = int(input())
km_litro = 12
distancia = horas * velocidade_media
total = distancia / km_litro
print('{:.3f}'.format(total))