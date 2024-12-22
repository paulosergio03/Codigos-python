#  Faça um programa que leia um número de 0 a 9999
#  e mostre na tela cada um dos dígitos separados.

n = int(input('Digite um número: '))
print(f'Analisando o número {n}')

u = (n % 10)
d = (n % 100 // 10)
c = (n % 1000 // 100)
m = (n % 10000 // 1000)

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Cetena: {c}')
print(f'Milhar: {m}')