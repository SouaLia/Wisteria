import pygame
import pygame as pg

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zoom até um limite em 3 segundos")

# Título do jogo
image = pygame.image.load("Bagunca/cutscene/teste/teste/WisteriaSlogan.png")
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Zoom
zoom_completed = False
zoom_factor = 1.0
zoom_max = 2.0  # Zoom máximo permitido
duration = 3000  # Tempo total do zoom (3 segundos)
start_time = pygame.time.get_ticks()

# Sequência de imagens
sequence_index = 0  # Índice da imagem atual
sequence_time = 100  # Tempo de mudança de frame 
last_switch_time = 0  # Tempo da última troca de imagem
sequence_images = [
    pygame.image.load("Bagunca/SpriteBegin/0.png"),
    pygame.image.load("Bagunca/SpriteBegin/1.png"),
    pygame.image.load("Bagunca/SpriteBegin/2.png"),
    pygame.image.load("Bagunca/SpriteBegin/3.png"),
    pygame.image.load("Bagunca/SpriteBegin/4.png"),
    pygame.image.load("Bagunca/SpriteBegin/5.png"),
    pygame.image.load("Bagunca/SpriteBegin/6.png"),
    pygame.image.load("Bagunca/SpriteBegin/7.png"),
    pygame.image.load("Bagunca/SpriteBegin/8.png"),
    pygame.image.load("Bagunca/SpriteBegin/9.png")
]
fade_duration = 2000  # Duração do fade-out (2 segundos)
fade_start_time = None  # Quando o fade começa
fade_alpha = 255  

running = True
while running:
    screen.fill((30, 30, 30))  # Fundo escuro para contraste

    # Calcula o tempo decorrido
    elapsed_time = pygame.time.get_ticks() - start_time

    if not zoom_completed:
        if elapsed_time < duration:
            progress = elapsed_time / duration
            zoom_factor = 1.0 + (zoom_max - 1.0) * progress
        else:
            zoom_factor = zoom_max
            zoom_completed = True
            last_switch_time = pygame.time.get_ticks()

        new_size = (int(image_rect.width * zoom_factor), int(image_rect.height * zoom_factor))
        zoomed_image = pygame.transform.smoothscale(image, new_size)
        new_rect = zoomed_image.get_rect(center=image_rect.center)
        screen.blit(zoomed_image, new_rect.topleft)

    else:
        
        screen.blit(zoomed_image, new_rect.topleft)

        current_time = pygame.time.get_ticks()
        if current_time - last_switch_time >= sequence_time:
            sequence_index += 1
            last_switch_time = current_time

            
        if current_time - last_switch_time >= sequence_time:
            if sequence_index < len(sequence_images) - 1:
                sequence_index += 1
                last_switch_time = current_time
            else:
                if fade_start_time is None:
                    fade_start_time = pygame.time.get_ticks()
                    
        if sequence_index < len(sequence_images):
            sequence_img = sequence_images[sequence_index]
            sequence_rect = sequence_img.get_rect(midleft=(WIDTH // 2.3 + 5, HEIGHT // 2 + 12))
            big_sequence_img = pg.transform.rotozoom(sequence_img, 0, 2.5)
            screen.blit(big_sequence_img, sequence_rect.topleft)
        
    clock = pygame.time.Clock()
    time = clock.get_time()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
