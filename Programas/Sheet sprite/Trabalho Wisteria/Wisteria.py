import pygame as pg
from pygame.locals import *

pg.init()
tela = pg.display.set_mode((800, 800))  
sprite = pg.image.load("Programas\Sheet sprite\Trabalho Wisteria\Wisteria.png")  
sair = False

x_sprite = 0
y_sprite = 50
wisteria_x = 100
wisteria_y = 400
relogio = pg.time.Clock() 

while not sair:
    tela.fill((0, 0, 0))
    tela.blit(sprite, (wisteria_x, wisteria_y), (x_sprite * 80, y_sprite, 80, 85))
    pg.display.flip()
    relogio.tick(4)
    tela.fill(0)
    
    #Controles do personagem

    for e in pg.event.get():
        if e.type == pg.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            sair = True
    #Detecta quando as teclas são pressionadas
    key = pg.key.get_pressed()

    #tecla da direita
    if key[K_RIGHT] :
        wisteria_x += 15
        y_sprite = 341
        x_sprite += 1.01

    #Tecla da esquerda
    elif key[K_LEFT]:
        wisteria_x -= 15
        y_sprite = 430
        x_sprite += 1.01
    else:
        if y_sprite == 430:
            y_sprite == 50
        elif y_sprite == 341:
            x_sprite = 800
            y_sprite = 400
        x_sprite += 1.01 #Foi adicionado 0.01 para enquadrar melhor os frames


    if x_sprite > 4:
        x_sprite = 0




