import pygame

pygame.init()

COLOR = [1, 1, 1]

while True:
    window = pygame.display.set_mode([715, 480])
    pygame.display.set_caption("Starship")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill(COLOR)
    pygame.display.update()
