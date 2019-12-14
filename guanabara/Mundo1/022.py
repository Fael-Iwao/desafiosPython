# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = str(input('Digite o nome da sua cidade: \n'))

print(city[:5].lower() == 'santo')