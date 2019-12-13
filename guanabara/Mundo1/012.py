# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Digite o salario: \n'))

increase = salary * 0.15

print('o salario no valor de  {} o valor de 15% de aumento é {} e no total fica {}'.format(salary, increase, (salary + increase)))