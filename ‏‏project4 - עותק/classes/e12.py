import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Moving rectangle")


x = 200
y = 200
y2 = 200

width = 30
height = 30

vel = 1

run = True

while run:

    pygame.time.delay(10)
    y += vel

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 0, 0), (5, y2, width, height))
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.draw.rect(win, (255, 0, 0), (450, y2, width, height))
    if y2 == 500:
        y2 = 0

    pygame.display.update()

pygame.quit()