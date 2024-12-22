# Conversor de temperaturas: escreva um programa que converta uma 
# temperatura digitada em ºC para ºF

c = float(input('Informe a temperatura em °C: ')) 

convesao = (c * 1.8) + 32
print(f'A temperatura de {c:.1f}°C corresnpode a {convesao:.1f}°F')