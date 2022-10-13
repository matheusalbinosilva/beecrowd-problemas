N = int(input())
resto = minutos = segundos = hora = 0

if N >= 3600:
    hora = N / 3600
    resto = (hora * 3600) - (hora.__floor__ () * 3600)
    if resto >= 60:
        minutos = resto / 60
        resto = (minutos * 60) - (minutos.__floor__() * 60)
        if resto >= 1:
            segundos = resto
elif N >= 60:
        minutos = N / 60
        resto = (minutos * 60) - (minutos.__floor__() * 60)
       
        if resto >= 1:
            segundos = resto
          
elif N >= 1:
            segundos = N
            minutos = 0

print('{}:{}:{}'.format(hora.__floor__(), minutos.__floor__(), segundos.__floor__()))