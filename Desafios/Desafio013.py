# Faça um algoritmo que leia o salário de um funcionário e mostre seu 
# novo salário, com 15% de aumento

salario = float(input('Qual é o seu salário R$'))

aumento = salario * 0.15
print(F'Seu salário atual é {salario:.2f} e com aumento de 15% ele passaram a ser {aumento+salario:.2f}')