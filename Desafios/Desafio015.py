# Aluguel de carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

dias = float((input('Quantos dias alugados? ')))
km = float(input('Quantos KM rodados? '))

aluguel = (dias * 60) + (km * 0.15) 
print(f'{aluguel:.2f}')