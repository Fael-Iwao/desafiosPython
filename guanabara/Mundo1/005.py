# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

a = int(input('Digite um número: \n'))

print('o numero digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format( a, (a * 2), (a * 3), pow(a, (1/2) ) ) )