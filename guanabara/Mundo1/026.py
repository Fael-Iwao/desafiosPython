# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint 

print('-='*26)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar')
print('-='*26)
print('\n')

numberThought = randint(0, 5)
number = int(input('em que número pensei? \n'))

if number == numberThought:
    print('Acertô mizerávi')
else:
    print('ERROOOOOOOOOU \n')
    print('o numero pensado foi {}'.format(numberThought) )

