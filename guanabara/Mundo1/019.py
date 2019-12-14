# O mesmo professor do desafio 018 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

name1 = str(input('Digite o nome do primeiro aluno \n'))
name2 = str(input('Digite o nome do segundo aluno \n'))
name3 = str(input('Digite o nome do terceiro aluno \n'))
name4 = str(input('Digite o nome do quarto aluno \n'))

names = [name1, name2, name3, name4]

shuffle(names)

print('a order dos alunos será')
print(names)