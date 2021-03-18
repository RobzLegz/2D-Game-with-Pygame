import pygame

pygame.init()

COLOR = [1, 1, 1]

ufo_image = pygame.image.load("ufo.png")

while True:
    window = pygame.display.set_mode([800, 500])
    pygame.display.set_caption("Starship")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("UP")
            if event.key == pygame.K_a:
                print("LIFT")
            if event.key == pygame.K_d:
                print("RIGHT")
            if event.key == pygame.K_s:
                print("DOWN")

    window.fill(COLOR)
    window.blit(ufo_image, [380, 210])
    pygame.display.update()
