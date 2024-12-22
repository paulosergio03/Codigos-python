# Um professor quer sortear um dos seus quatro 
# alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido.

import random

aluno1 = input('Digite o nome do priemiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quatro aluno: ')
aluno5 = input('Digite o nome do quinto aluno: ')

lista = [aluno2, aluno2, aluno3,aluno4, aluno5]

escolhido = random.choice(lista)

print(f'O aluno soteador foi: {escolhido}')


