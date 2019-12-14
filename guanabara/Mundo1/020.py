#  Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

name = str(input('Digite o seu nome completo  \n')).strip()

nameSplited = name.split()

print('Seu nome completo em maiusculas é {}'.format(name.upper()))
print('Seu nome completo em minusculas é {}'.format(name.lower()))
print('Seu nome completo tem {} letras'.format( len(name) - name.count(' ') ) )
print('Seu primeiro nome tem é {} e tem {} letras'.format(nameSplited[0], len(nameSplited[0])))

