import pygame

pygame.init()

COLOR = [1, 1, 1]

ufo_image = pygame.image.load("ufo.png")

x_pos = 0
y_pos = 0

while True:
    window = pygame.display.set_mode([800, 500])
    pygame.display.set_caption("Starship")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_pos -= 10
            elif event.key == pygame.K_a:
                x_pos -= 10
            elif event.key == pygame.K_d:
                x_pos += 10
            elif event.key == pygame.K_s:
                y_pos += 10

    window.fill(COLOR)
    window.blit(ufo_image, [x_pos, y_pos])
    pygame.display.update()
