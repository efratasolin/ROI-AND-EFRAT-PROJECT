import pygame
from pygame import mixer
import random
from Train import Train
from Player import *

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

# def display_score(self):
#     font = pygame.font.SysFont('ariel', 30)
#     score = font.render(f"score:{self.}", True, (0, 0, 0))
#     self.surface.blit(score, (400, 10))


def draw_obstacles(lanes):
    train9 = 0
    train7 = 0
    train6 = 0
    if 0 in lanes:
        # pygame.draw.rect(win, (250, 0, 0), (0, obstacle_y, Obstacle_in_width, Obstacle_in_height))
        img1 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\TRAIN.png")
        img1 = pygame.transform.scale(img1, (120, 120))
        train9 = Train(LANE1_X, obstacle_y, img1)
        win.blit(train9.img_src, (train9.x, train9.y))

    if 1 in lanes:
        # pygame.draw.rect(win, (250, 0, 0), (255, obstacle_y, Obstacle_in_width, Obstacle_in_height))
        img2 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\TRAIN2.png")
        img2 = pygame.transform.scale(img2, (160, 160))
        train6 = Train(LANE2_X, obstacle_y, img2)
        win.blit(train6.img_src, (train6.x, train6.y))

    if 2 in lanes:
        # pygame.draw.rect(win, (250, 0, 0), (425, obstacle_y, Obstacle_in_width, Obstacle_in_height))
        img3 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\TRAIN.png")
        img3 = pygame.transform.scale(img3, (120, 120))
        train7 = Train(LANE3_X, obstacle_y, img3)
        win.blit(train7.img_src, (train7.x, train7.y))
    return train9, train6, train7

# set the pygame window name
pygame.display.set_caption("ROI AND EFRAT")

player_x = 135
player_y = 250
obstacle_y = 0

LANE1_X = 0
LANE2_X = 165
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
   # test_rect = pygame.Rect(player_rect.top - 1)
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.

        # for test in list_ofspike:
        #     if test_rect.colliderect(spike):
        #         pygame.QUIT()

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
    text_size = 40
    text = str(timer)
    color = (0, 0, 0)
    font = pygame.font.SysFont(font_name, text_size)
    win.blit(font.render(text, True, color), (410, 20))
    timer += 1

    if obstacle_y == 500:
        obstacle_y = 0

    print(obstacle_y)
    if obstacle_y >= 500 or obstacle_y <= 0:
        lanes = random.sample(range(0, 3), 2)
    train9,train6,train7 = draw_obstacles(lanes)

    obstacle_y += vel

    # pygame.draw.rect(win, (255, 0, 0), (0, obstacle_y, Obstacle_in_width, Obstacle_in_height))
    # pygame.draw.rect(win, (0, 255, 0), (player_x, player_y, width, height))
    # player_rect = pygame.Rect(50, 50, 25, 25)
    img4 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\JAKE.png")
    img4 = pygame.transform.scale(img4, (width, height))
    win.blit(img4, (player_x, player_y))

    TRAIN_LENGTH = 150
    TRAIN_HEIGHT = 100

    if train6 != 0:
        if train6.x < player_x < train6.x + TRAIN_LENGTH:
            if train6.y < player_y < train6.y + TRAIN_HEIGHT:
                run = False
    if train7 != 0:
        if train7.x < player_x < train7.x + TRAIN_LENGTH:
            if train7.y < player_y < train7.y + TRAIN_HEIGHT:
                run = False
    if train9 != 0:
        if train9.x < player_x < train9.x + TRAIN_LENGTH:
            if train9.y < player_y < train9.y + TRAIN_HEIGHT:
                run = False

    # pygame.draw.rect(win, (255, 0, 0), (425, obstacle_y, Obstacle_in_width, Obstacle_in_height))
    # pygame.draw.rect(win, (255, 0, 0), (225, obstacle_y, Obstacle_in_width, Obstacle_in_height))
    # if obstacle_y == 500:
    #     obstacle_y = 0

    # if y == 0:
    #     y = 500

    pygame.display.update()
    #pygame.display.flip()

pygame.quit()