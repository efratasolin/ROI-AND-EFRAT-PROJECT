import pygame
from pygame import mixer
import random

pygame.init()
timer = 0
mixer.init()
mixer.music.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\song.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))

img = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\backgroundd.jpeg")
img = pygame.transform.scale(img, (500, 500))
win.blit(img, (0, 0))


def draw_obstacles(lanes):
    if 0 in lanes:
        # pygame.draw.rect(win, (250, 0, 0), (0, obstacle_y, Obstacle_in_width, Obstacle_in_height))
        img1 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\TRAIN.png")
        img1 = pygame.transform.scale(img1, (120, 120))
        win.blit(img1, (LANE1_X, obstacle_y))

    if 1 in lanes:
        # pygame.draw.rect(win, (250, 0, 0), (255, obstacle_y, Obstacle_in_width, Obstacle_in_height))
        img2 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\TRAIN.png")
        img2 = pygame.transform.scale(img2, (120, 120))
        win.blit(img2, (LANE2_X, obstacle_y))

    if 2 in lanes:
        # pygame.draw.rect(win, (250, 0, 0), (425, obstacle_y, Obstacle_in_width, Obstacle_in_height))
        img3 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\TRAIN.png")
        img3 = pygame.transform.scale(img3, (120, 120))
        win.blit(img3, (LANE3_X, obstacle_y))


# set the pygame window name
pygame.display.set_caption("ROI AND EFRAT")

player_x = 250
player_y = 250
obstacle_y = 0

LANE1_X = 0
LANE2_X = 200
LANE3_X = 400
LANE_DISTANCE = 200

lanes = []

# dimensions of the object
width = 230
height = 230

Obstacle_in_width = 75
Obstacle_in_height = 75

# velocity / speed of movement
vel = 2.5
vel2 = 25
# Indicates pygame is running
run = True

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)
    # y -= vel
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > LANE1_X:
        player_x -= LANE_DISTANCE

    if keys[pygame.K_RIGHT] and player_x < LANE3_X:
        player_x += LANE_DISTANCE

    win.fill((0, 0, 0))
    img = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\backgroundd.jpeg")
    img = pygame.transform.scale(img, (500, 500))
    win.blit(img, (0, 0))

    font_name = "Arial"
    text_size = 20
    text = str(timer)
    color = (0, 255, 120)
    x_pos = 50
    y_pos = 100
    font = pygame.font.SysFont(font_name, text_size)
    win.blit(font.render(text, True, color), (50, 450))
    timer += 1

    if obstacle_y == 500:
        obstacle_y = 0

    print(obstacle_y)
    if obstacle_y >= 500 or obstacle_y <= 0:
        lanes = random.sample(range(0, 3), 2)
    draw_obstacles(lanes)

    obstacle_y += vel

    # pygame.draw.rect(win, (255, 0, 0), (0, obstacle_y, Obstacle_in_width, Obstacle_in_height))
    # pygame.draw.rect(win, (0, 255, 0), (player_x, player_y, width, height))
    img4 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\JAKE.png")
    img4 = pygame.transform.scale(img4, (width, height))
    win.blit(img4, (player_x, player_y))

    # pygame.draw.rect(win, (255, 0, 0), (425, obstacle_y, Obstacle_in_width, Obstacle_in_height))
    # pygame.draw.rect(win, (255, 0, 0), (225, obstacle_y, Obstacle_in_width, Obstacle_in_height))
    # if obstacle_y == 500:
    #     obstacle_y = 0

    # if y == 0:
    #     y = 500

    pygame.display.update()

pygame.quit()