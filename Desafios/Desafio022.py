# Crie um programa que leia o nome completo de uma pessoa:
nome = input('Digite o seu nome completo: ')

# O nome com todas as letras maiúsculas
print(nome.upper())

# O nome com todas minúsculas
print(nome.lower())

# Quantas letras ao todo (sem considerar espaços)
print(len(nome))

# Quantas letras tem o primeiro nome: 
print(len(nome.split()[0]))
