
lista = [{"codigo":1, "preço":4.00}, 
            {"codigo":2, "preço":4.50},
            {"codigo":3, "preço":5.00}, 
            {"codigo":4, "preço":4.00},
            {"codigo":5, "preço":1.50}]

cod, quant = input().split(' ')
cod = int(cod)
quant = int(quant)
for p, v in enumerate(lista):
    if v['codigo'] == cod:
        total = v['preço'] * quant
   
print(f'Total: R$ {total:.2f}')
    


