# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: \n')

print('seu tipo primitivo: ', type(a))
print('é somente espaços? ', a.isspace())
print('é alfabetico? ', a.isalpha())
print('é somente numeros? ', a.isalnum())
print('é somente minusculas? ', a.islower())
print('é somente maiusculas? ', a.isupper())
print('esta capitalizada? ', a.istitle())