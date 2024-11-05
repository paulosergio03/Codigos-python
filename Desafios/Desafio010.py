#Crie um aprograma que leia
#quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar

real = float(input('Quanto você tem R$: ')) 

dolar = real / 5.78


print(f'Com R${real} você pode comprar {dolar:.2F}USD')