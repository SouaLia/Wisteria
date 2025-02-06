import pygame
from pygame.locals import *
from sys import exit

#Classe base para rodar a tela

class Tela:

    #definição de variáveis
    largura = 900
    altura = 650
    titulo = "Wisteria - A bruxa aventureira"

    FPS = 60


    #função de limite da tela
    def __init__(self, largura = 900, altura = 650, titulo = "Wisteria - A bruxa aventureira"):
        pygame.init()
        self.largura = largura 
        self.altura = altura
        self.tela = pygame.display.set_mode((self.largura, self.altura)) #já atribui a variável como altura e largura da tela
        pygame.display.set_caption(titulo) #pre define o titulo
        
        self.relogio= pygame.time.Clock()
        self.rodando= True



    #função que permite o fechamento da tela
    def eventos(self):
        #captura o evento de fechar a tela
        for evento in pygame.event.get():
            if evento.type == QUIT:
                self.rodando = False



    def atualizar(self):
        pass #atualiza o jogo




    def fundo(self):
        self.tela.fill((0))# o fundo da tela fica preto



    def roda (self, FPS = 60):
        while self.rodando:
            self.eventos()
            self.atualizar()
            self.fundo()
            pygame.display.update()
            self.relogio.tick(FPS)
        pygame.quit()
        exit()

#para testar e ver se funciona
if __name__ == "__main__" :
    jogo = Tela()
    jogo.roda()


