# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Digite o preço do produto: \n'))

discount = price * 0.05

print('o produto no valor de  {} o valor de 5% de desconto é {} e no total fica {}'.format(price, discount, (price - discount)))