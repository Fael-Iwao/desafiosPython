#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angle = float(input('Digite o ângulo: \n'))

valSin = sin(radians(angle))
valCos = cos(radians(angle))
valTan = tan(radians(angle))

print('O angulo de {} tem \n o Seno de {:.2f}, \n o Cosseno de {:.2f} \n e a Tangente de {:.2f}'.format(angle, valSin, valCos, valTan))
