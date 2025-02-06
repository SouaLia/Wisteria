# imports
import pygame
from pygame.locals import * 
from sys import exit 

# tela
largura = 900
altura = 750

tela = pygame.display.set_mode((largura, altura))

# loop infinito
while True:
    # checa se algum evento ocorre
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()      #sai do loop
            
    pygame.display.update()     #atuaçiza a tela 