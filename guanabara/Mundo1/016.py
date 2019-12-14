#  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

a = int(input('Digite o cateto oposto: \n'))
b = int(input('Digite o cateto adjascente \n'))
c = hypot(a, b)
print('a hipotenusa mede: {: .2f}'.format(c))
