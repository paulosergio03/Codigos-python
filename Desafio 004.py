#Faça um programa que leia algo
#pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações
#possiveis sobre ele.

n = (input(' Digite algo: '))
print(f'Qual é o tipo? {type(n)}')
print(f'É somente espaço? {n.isspace()}')
print(f'Está capitalizada? {n.istitle()}')
print(f'Ele é alphanumerico? {n.isalnum()}')
print(f'Ele é maiusculo? {n.isupper()}')
print(f'Está em minúsculas? {n.islower()}')
print(f'Ele é alfabetico? {n.isalpha()}')
print(f'É um número? {n.isnumeric()}')