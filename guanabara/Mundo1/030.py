# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

year = int(input('digite o ano'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('o ano {} é bissexto'.format(year))
else:
    print('o ano {} não é bissexto'.format(year))  