#Crie um programa que leia a
#altura e a largura de uma
#parede por metros,calcule a sua área e a quantidade
#quantidade de tinta necessária para pinta-lá


largura = float(input('Digite a largura da parede em metros: '))
altura = float (input('Digite a altura da parede em metros: '))

dimensão = largura * altura 
tinta = 2
litros = dimensão/tinta
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {dimensão}m² é necessário comprar {litros}L de tinta')