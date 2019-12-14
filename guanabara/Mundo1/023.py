#  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Digite o nome completo \n')).strip()

print('Seu nome possui "SILVA"? {}'.format('SILVA' in name.upper().split()))