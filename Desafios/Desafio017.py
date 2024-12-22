# Desafio 17: Faça um programa que leia o comprimento do 
# cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa.

from math import sqrt,hypot

#co = float(input('Digite o cateto oposto: '))
#ca = float(input('Digite o cateto adjacente: '))

#hi = sqrt(co ** 2 + ca ** 2)

#print(f'A hipotenusa vai medir {hi:.2f}')


co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hi = hypot(co, ca)

print(f'A hipotenusa vai medir {hi:.2f}')




