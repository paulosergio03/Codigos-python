#Crie um algoritmo que leia o preço de um produto
#e mostre o novo preço com desconto de 5% de desconto

produto = float(input('Qual o preço do produto R$'))

desconto = produto*0.05

print(f'O produto que custava {produto} com o desconto de 5% vai custar R${produto-desconto:.2f}')