import os
import random
import math
import pygame
from os import listdir
from os.path import isfile,join
from pygame.locals import * 
from sys import exit 
#----------------------------------------

#O motivo de adição do os: aprimorar a adição de imagens sem a complicação do path

pygame.init()

pygame.display.set_caption("Plataformer")
WIDTH,HEIGHT= 800,800

tela = pygame.display.set_mode((WIDTH,HEIGHT))
cores = {
    'branco':(255,255,255),
    'preto' : (0,0,0),
    'vermelho' : (155,0,0)
}
FPS = 60

def get_fundo(name):
    image = pygame.image.load(join("cenario","game_files", "background",name))
    _,_,width,height = image.get_rect()
    tiles = []
    for i in range (WIDTH // width + 1):
        for j in range (HEIGHT // height + 1):
            pos = [i * width, j *height]
            tiles.append(pos)
    return tiles, image
    

def main(tela):

    clock = pygame.time.Clock()
    fundo,f_image = get_fundo("background 1.png")

    run = True

    #Loop do jogo
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() 
                exit()  
    #-------------------------------------
if __name__ == "__main__":
    main(tela) #A função só ira ser passada se esse arquivo rodar, se nçao, o jogo não rodará.


