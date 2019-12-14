# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Digite o nome completo \n')).strip()

names = name.split()

print('O primeiro nome é {} e o ultimo nome é {}'.format(names[0], names[-1]))