import pygame

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zoom até um limite em 5 segundos")

# Carregar imagem
image = pygame.image.load("teste\imagem.png")  # Substitua pelo caminho da sua imagem
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Variáveis de zoom
zoom_factor = 1.0
zoom_max = 2.0  # Zoom máximo permitido (2x)
duration = 5000  # Tempo total do zoom (5 segundos)
start_time = pygame.time.get_ticks()  # Marca o tempo inicial

running = True
while running:
    screen.fill((30, 30, 30))  # Fundo escuro para contraste

    # Calcula o tempo decorrido
    elapsed_time = pygame.time.get_ticks() - start_time

    # Se ainda estamos dentro do tempo da animação, calculamos o zoom progressivo
    if elapsed_time < duration:
        progress = elapsed_time / duration  # Normaliza para um valor entre 0 e 1
        zoom_factor = 1.0 + (zoom_max - 1.0) * progress  # Ajusta o zoom progressivamente
    else:
        zoom_factor = zoom_max  # Fixa o zoom no máximo após 5 segundos

    # Redimensiona a imagem conforme o fator de zoom
    new_size = (int(image_rect.width * zoom_factor), int(image_rect.height * zoom_factor))
    zoomed_image = pygame.transform.smoothscale(image, new_size)

    # Reajusta a posição para centralizar a imagem redimensionada
    new_rect = zoomed_image.get_rect(center=image_rect.center)
    
    # Desenha a imagem na tela
    screen.blit(zoomed_image, new_rect.topleft)

    pygame.display.flip()  # Atualiza a tela

    # Eventos do pygame (para fechar a janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
