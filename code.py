import pygame
pygame.init()
size = w, h = 250, 250
x, y = 0, 0
x_, y_ = 0, 0
screen = pygame.display.set_mode(size)
running, moving = True, False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 100:
                moving = True
        if event.type == pygame.MOUSEMOTION:
            if moving:
                x_, y_ = event.rel
                x += x_
                y += y_
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            moving = False
    pygame.draw.rect(screen, (250, 0, 0), (x, y, 80, 80))
    pygame.display.flip()
    screen.fill((0, 0, 0))
pygame.quit()
