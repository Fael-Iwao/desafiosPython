# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celcius = int(input('Digite a temperatura em celcius: \n'))

fahrenheit = 9 * celcius / 5 + 32

print(' {}º C  correspondem a {}º F'.format(celcius, fahrenheit))