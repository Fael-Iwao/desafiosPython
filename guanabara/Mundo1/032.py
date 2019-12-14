# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Digite o salario: \n'))

if salary < 1251 :
    increase = salary * 0.15
    percent = '15%'
else:
    increase = salary * 0.10
    percent = '10%'


print('seu salario com aumento de {:.2f} correspondente a {}  é de {:.2f}'.format(increase, percent, (salary + increase)))

