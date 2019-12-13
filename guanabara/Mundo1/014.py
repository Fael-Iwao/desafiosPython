# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Digite a quantidade de kms rodados: \n'))
days = int(input('Digite a quantidade de dias \n'))

costPerDay = days * 60
costPerKm = km * 0.15
total  = costPerDay + costPerKm

print(' O custo do carro por {} dias é {}, \n o custo de {} km rodados é {}, \n ficando um total de {}'.format(days, costPerDay, km, costPerKm, total))
