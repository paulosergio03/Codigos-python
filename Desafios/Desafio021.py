# Duas formas de executar o mp3 no python
# Modulo playsound e pygame
# playsound use ( \\ ) ao invés de ( \ )
# para instalar o modulo do playsound pip install playsound==1.2.2

# Funcionou no vscode
from playsound import playsound
playsound('C:\\Users\\Paulo&Sara\\PycharmProjects\\teste\\Desafios\\ex01.mp3')

# Funcionou no pycharm
#import pygame
#pygame.mixer.init()
#pygame.mixer.music.load('ex01.mp3')
#pygame.mixer.music.play()
#input()
#pygame.event.wait()