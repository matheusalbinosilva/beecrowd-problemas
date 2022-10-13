class Candidatos:
    def __init__(self, nome, votos):
        self.nome = nome
        self.votos = votos


eleitores = int(input('Digite o numero total de eleitores: '))
print('_='*10)
print('''CANDITADO 1 = 13
CANDITADO 2 = 22
CANDITADO 3 = 12''')
print('_='*10)
contador = 0
candidato1 = candidato2 = candidato3 = total_votos = 0
while eleitores != contador:
    voto = int(input('Digite o numero do seu canditado: '))
    while voto != 13 and voto != 22 and voto != 12:
        voto = int(input(('Digite apenas 13 /22 /12: ')))
        if voto == 13 and voto == 22 and voto == 12:
            break
        
    if voto == 13:
            candidato1 = candidato1 + 1
    if voto == 22:
            candidato2 = candidato2 + 1
    if voto == 12:
            candidato3 = candidato3 + 1
    contador = contador + 1
print(f'Lula recebeu {candidato1} votos ')
print(f'Bolsonaro recebeu {candidato2} votos')
print(f'Ciro Gomes recebeu {candidato3} votos')

maior = candidato1
if candidato2 > candidato1:
    maior = candidato2
if candidato3 > maior:
    maior = candidato3
c1 = Candidatos('Lula', candidato1)
c2 = Candidatos('Bolsonaro', candidato2)
c3 = Candidatos('Ciro Gomes', candidato3)
print('O vencedor foi ', end='')
if maior == candidato1:
    print(c1.nome)
if maior == candidato2:
    print(c2)
if maior == candidato3:
    print(c3)
