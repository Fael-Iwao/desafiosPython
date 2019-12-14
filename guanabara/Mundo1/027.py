# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('-='*26)
print('programa de multas')
print('-='*26)
print('\n')

speed = float(input('digite a velocidade do carro: \n'))

speedLimit = 80

if speed > speedLimit:
    penalty = (speed - speedLimit) * 7
    print('Multado! sua multa custa R${:.2f}'.format(penalty))
else:
    print('Passou') 

