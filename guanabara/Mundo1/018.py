# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

name1 = str(input('Digite o nome do primeiro aluno \n'))
name2 = str(input('Digite o nome do segundo aluno \n'))
name3 = str(input('Digite o nome do terceiro aluno \n'))
name4 = str(input('Digite o nome do quarto aluno \n'))

names = [name1, name2, name3, name4]

chosen = choice(names)

print('o Aluno escolhido foi {}'.format(chosen))