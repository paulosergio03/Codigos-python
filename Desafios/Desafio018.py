# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
# cosseno e tangente desse ângulo.

from math import radians,sin,cos,tan

angulo = float(input('Digite o ângulo que você deseja: '))

sen = sin(radians(angulo))
co = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O seno do ângulo {angulo}° é {sen:.2f}')
print(f'O cosseno do ângulo {angulo}° é {co:.2f}')
print(f'A tangente ddo ângulo {angulo}° é {tangente:.2f}')

