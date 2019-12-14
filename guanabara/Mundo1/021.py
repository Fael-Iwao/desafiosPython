#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número: \n'))

unity = num // 1 % 10
ten = num // 10 % 10
hundred = num // 100 % 10
thousands = num // 1000 % 10

print('o numero é {}'.format(num))
print('a unidade é {}'.format(unity))
print('a dezena é {}'.format(ten))
print('a centena é {}'.format(hundred))
print('o milhar é {}'.format(thousands))