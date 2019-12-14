#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

phrase = str(input('Digite uma frase \n')).lower().strip()

print('a letra A apareceu {} vezes '.format( phrase.count('a') ) )
print('a primeira posição que aparece é  {}'.format( phrase.find('a') + 1 ) )
print('a ultima posição que aparece {}'.format( phrase.rfind('a') + 1 ) )