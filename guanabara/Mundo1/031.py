# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
num3 = int(input('Digite o terceiro número:'))
numbers = [num1, num2, num3]

print('O maior valor digitado foi {}'.format(max(numbers)))
print('O menor numero digitado foi {}'.format(min(numbers)))