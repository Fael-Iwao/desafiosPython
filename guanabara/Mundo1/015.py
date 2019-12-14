#  Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

a = float(input('Digite um número: \n'))

print(' o numero digitado foi {} e sua porção inteira é {}'.format(a, trunc(a)))