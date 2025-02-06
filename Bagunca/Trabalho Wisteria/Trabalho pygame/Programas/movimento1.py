# imports
import pygame
from pygame.locals import * 
from sys import exit 

# tela
largura = 900
altura = 650

#movimento
x = largura/2
y = altura/2

tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

# loop infinito
while True:
    #frames por segundo
    relogio.tick(50)

    # "apaga" a tela
    tela.fill((0, 0, 0))
    
    # checa se algum evento ocorre
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            exit()      #sai do loop
        
    #Movimentação 
        '''TRAVADA if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20 #esquerda
            if event.key == K_d:
                x = x + 20 #direita 
            if event.key == K_w:
                y = y - 20  #cima
            if event.key == K_s:
                y = y + 20 #baixo'''
    # SUAVE
    if pygame.key.get_pressed()[K_a]:
        x = x - 10  # esquerda 
    if pygame.key.get_pressed()[K_d]:
        x = x + 10  #direita
    if pygame.key.get_pressed()[K_w]:
        y = y - 10  #cima
    if pygame.key.get_pressed()[K_s]:
        y = y + 10  #baixo
    # desenha na tela
    pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50))

    #objeto se mover oszinho
   # if y >= altura:
    #    y = 0
   # y = y + 5

    pygame.display.update()     #atuaçiza a tela 