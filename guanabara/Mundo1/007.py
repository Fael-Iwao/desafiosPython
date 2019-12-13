# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.


meters = float(input('Digite a quantidade de metros: \n'))

cm = meters * 100
mm = meters * 1000

print('{} metros em centimetros é {} e em milimetros é {}'.format(meters, cm, mm) )