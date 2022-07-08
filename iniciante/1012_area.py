linha_1 = input().split(' ')

a, b, c = linha_1

valor_a = float(a)
valor_b = float(b)
valor_c = float(c)

PI = 3.14159

area_tringulo = (valor_a * valor_c) / 2
area_circulo =  PI * valor_c ** 2
area_trapezio = (valor_a + valor_b) * valor_c / 2
area_quadrado = (valor_b) * (valor_b)
area_retangulo = valor_a * valor_b

print('TRIANGULO: {:.3f}'.format(area_tringulo))
print('CIRCULO:. {:.3f}'.format(area_circulo))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_retangulo))







