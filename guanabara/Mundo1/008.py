#  Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

number = int(input('Digite um numero e veja a tabuada dele: \n'))

count = 0
while (count < 11):
    print('{} x {} = {}'.format(number, count, (number * count)) )
    count += 1
