import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 900
altura = 650
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo com Movimento de Cenário")

relogio = pygame.time.Clock()

cenarios = [
    pygame.image.load("game_files/background 1/background 1.png"),
    pygame.image.load("game_files/background 2/Plan 1.png"),
    pygame.image.load("game_files/background 3/background 3.png"),
    pygame.image.load("game_files/background 4/background 4.png")
]

cenarios = [pygame.transform.scale(c, (largura, altura)) for c in cenarios]

cenario_atual = 0

personagem = pygame.Rect(100, altura // 2, 40, 50)
velocidade = 10

while True:
    relogio.tick(50)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()
    if keys[K_a] and personagem.x > 0:
        personagem.x -= velocidade
    if keys[K_d] and personagem.x < largura - personagem.width:
        personagem.x += velocidade
    if keys[K_w]:
        personagem.y -= velocidade
    if keys[K_s]:
        personagem.y += velocidade
    
    if personagem.x >= largura - personagem.width:
        if cenario_atual < len(cenarios) - 1:
            cenario_atual += 1
            personagem.x = 0  
    elif personagem.x < 0:
        if cenario_atual > 0:
            cenario_atual -= 1
            personagem.x = largura - personagem.width  
    
    tela.fill((0, 0, 0))
    tela.blit(cenarios[cenario_atual], (0, 0))
    
    pygame.draw.rect(tela, (255, 0, 0), personagem)
    
    pygame.display.update()
