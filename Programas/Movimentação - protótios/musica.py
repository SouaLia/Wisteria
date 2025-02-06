import random
import pygame
from pygame.locals import *
from sys import exit

#inicialização
pygame.init()

#mudica
pygame.mixer.music.set_volume(0.5)
mscFundo = pygame.mixer.music.load('IframeBreatheintheruins,Squire.mp3')
pygame.mixer.music.play(-1) #a musica toda repetidamente

somEstrela = pygame.mixer.Sound('Twinklesparkle.wav')

#tela
largura = 900
altura = 650        #tamanho da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Wisteria, a bruxa aventureira")     #nomezinho no topo
relogio = pygame.time.Clock()

#texto
fonte = pygame.font.SysFont('Arial', 50, True, False)
#pontuação
pontos = 0

#posições iniciais
x, y = int(largura / 2), int(altura / 2)
x_estrela = random.randint(50, 800)
y_estrela = random.randint(50, 600)

#loop 
while True:
    relogio.tick(50)
    tela.fill((0, 0, 0))

    #texto
    mensagem = f"Estrelas: {pontos}"
    texto_form = fonte.render(mensagem, True, (255, 255, 255))
    tela.blit(texto_form, (450, 40))

    #rventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #movimentação suave
    keys = pygame.key.get_pressed()
    if keys[K_a]: x -= 10
    if keys[K_d]: x += 10
    if keys[K_w]: y -= 10
    if keys[K_s]: y += 10

    #Limita a posicao do personagem
    x = max(0, min(largura - 40, x))
    y = max(0, min(altura - 50, y))

    #desenha retângulos
    jogador = pygame.draw.rect(tela, (255, 0, 255), (x, y, 40, 50))
    estrela = pygame.draw.rect(tela, (0, 0, 255), (x_estrela, y_estrela, 40, 50))

    #Colisão
    if jogador.colliderect(estrela):
        somEstrela.play()       #faz um som
        pontos += 1             #calc pontos
        #muda a posicao da estrela
        x_estrela = random.randint(50, 800)
        y_estrela = random.randint(50, 600)

    # Atualizar tela
    pygame.display.update()