'''
 Alunas: Akilanny Silva Cruz, Cecilia Tavares Barreto, Vitória Lima 
 Professora: Alessandra Aguiar V.
 Programação III

 Wisteria, a bruxa aventureira
'''

#imports
import random
import pygame
from pygame.locals import *
from sys import exit

#inicialização
pygame.init()

#musica e sons de fundo 
pygame.mixer.music.set_volume(0.5)
mscFundo = pygame.mixer.music.load('IframeBreatheintheruins,Squire.mp3')
pygame.mixer.music.play(-1)     #a musica toda repetidamente

somEstrela = pygame.mixer.Sound('Twinklesparkle.wav')

#tela
largura = 900
altura = 650        #tamanho da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Wisteria, a bruxa aventureira")     #nomezinho no topo

#fps e etc
relogio = pygame.time.Clock()  
fps = 50

#texto
fonte = pygame.font.SysFont('Arial', 20, True, False)

#pontuação
pontos = 0

#criacoes de personagem e posições iniciais
class Wisteria(pygame.sprite.Sprite):
    def __init__(self, x, y, tam, speed):
        super().__init__()  #inicializa a classe

        self.speed = speed    #quantos pixeis vai se mexr
        
        self.direcao = 1 #direcao do personagem   1 =  direita, -1 = esquerda 
        self.flip = False

        img = pygame.image.load('perso.png')  #carrega a imagem MUDARRRRRRRR
        self.img = pygame.transform.scale(img, (int(img.get_width() * tam), int(img.get_height() * tam)))  #redimensiona a imagem
        self.rect = self.img.get_rect()  #cria o retângulo a partir da imagem
        self.rect.center = (x, y)  #posiciona o centro da tela
        
    def move(self, esquerda, direita):
        #reseta as variaveis de movimento
        dx = 0
        dy = 0
        #define o movimento
        if esquerda:
            dx = - self.speed
            self.flip = True
            self.direcao = -1
        if direita: 
            dx = self.speed
            self.flip = False
            self.direcao = 1

        #muda a posicao do retanfulo
        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)  #desenha o sprite na superfície fornecida, com ele podendo virar

player = Wisteria(200, 200, 3, 5)  #chama a class Wisteria com esses valores

'''x_estrela = random.randint(50, 800)
y_estrela = random.randint(50, 600)'''

#ações do personagem 
esquerda = False
direita = False

#loop 
partida = True
while partida:
    relogio.tick(fps)
    tela.fill((0, 0, 0)) #tudo preto

    
    #eventos
    for event in pygame.event.get():
         # saida do jogo
        if event.type == QUIT:
            partida = False
        
        #controles (movimentacao, saida)
        if event.type == KEYDOWN:
            if event.key == K_a:   
                esquerda = True
            if event.key == K_d:
                direita = True

            if event.key == K_ESCAPE: #se apertar ESC sai 
                partida = False

        if event.type == KEYUP:
            if event.key == K_a:
                esquerda = False
            if event.key == K_d:
                direita = False

    #texto
    mensagem = f"Estrelas: {pontos}"
    texto_form = fonte.render(mensagem, True, (255, 255, 255))
    tela.blit(texto_form, (750, 40))
              
    # aparece o personagem
    player.draw(tela)
    player.move(esquerda, direita)

    '''#Limita a posicao do personagem
    x = max(0, min(largura - 40, x))
    y = max(0, min(altura - 50, y))

    #Colisão
    if jogador.colliderect(estrela):
        somEstrela.play()       #faz um som
        pontos += 1             #calc pontos
        #muda a posicao da estrela
        x_estrela = random.randint(50, 800)
        y_estrela = random.randint(50, 600)'''

    # Atualizar tela
    pygame.display.update()