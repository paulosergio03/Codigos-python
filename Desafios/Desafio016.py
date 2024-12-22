# Crie um programa que leia um número real qualquer 
# pelo teclado e mostre na tela a sua porção inteira.

import math
num = float(input('Digite um número: '))
inteiro = math.trunc(num)

print(f'O número {num} tem a parte inteira {inteiro}')