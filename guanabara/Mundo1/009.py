# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# $ = 4.11

a = float(input('Digite o o valor em reais: \n'))

print('R$ {} em US$ são {: .2f}'.format(a, (a / 4.11)))