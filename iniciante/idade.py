from math import floor
dias_vida = int(input())

ano = resto = meses = dia = 0
if dias_vida >= 365:
    ano = dias_vida / 365
    resto = (ano * 365) - (ano.__floor__() * 365)
    if resto >= 30:
        meses = resto / 30
        resto = (meses * 30) - (meses.__floor__()  * 30)
        if resto >= 1:
            dia = resto
            
elif dias_vida >= 30:
    meses = dias_vida / 30
    resto = (meses * 30) - (meses.__floor__()  * 30)
    if resto >= 1:
        dia = resto
elif resto >= 1:
    dia = resto
print('{} ano (s)'.format(ano.__floor__()))
print('{} mes (es)'.format(meses.__floor__()))
print('{} dia (s)'.format(dia.__floor__()))



    
