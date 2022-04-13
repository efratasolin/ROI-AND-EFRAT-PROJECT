import pygame
from pygame import mixer
import random
import time
from Train import Train
from Player import *
from Constans import *

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
    train9 = 0
    train7 = 0
    train6 = 0
    if 0 in lanes:
        img1 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\TRAIN.png")
        img1 = pygame.transform.scale(img1, (120, 120))
        train9 = Train(LANE1_X, obstacle_y, img1)
        win.blit(train9.img_src, (train9.x, train9.y))

    if 1 in lanes:
        img2 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\TRAIN2.png")
        img2 = pygame.transform.scale(img2, (160, 160))
        train6 = Train(LANE2_X, obstacle_y, img2)
        win.blit(train6.img_src, (train6.x, train6.y))

    if 2 in lanes:
        img3 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\TRAIN.png")
        img3 = pygame.transform.scale(img3, (120, 120))
        train7 = Train(LANE3_X, obstacle_y, img3)
        win.blit(train7.img_src, (train7.x, train7.y))
    return train9, train6, train7

# set the pygame window name
pygame.display.set_caption("ROI AND EFRAT")

lanes = []

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
    train9, train6, train7 = draw_obstacles(lanes)

    obstacle_y += vel

    img4 = pygame.image.load("C:\\Users\\User\\PycharmProjects\\project999999999999999\\project4\\JAKE.png")
    img4 = pygame.transform.scale(img4, (width, height))
    win.blit(img4, (player_x, player_y))
    print(player_x)
    if train6 != 0:
        if train6.x - TRAIN_LENGTH < player_x and player_x < train6.x:
            if train6.y < player_y and player_y < train6.y + TRAIN_HEIGHT:
                print('6')
                print(train6.x)
                print(train6.y)
                print(player_x)
                print(player_y)
                run = False
    if train7 != 0:
        if train7.x - TRAIN_LENGTH < player_x and player_x < train7.x:
            if train7.y < player_y and player_y < train7.y + TRAIN_HEIGHT:
                print('7')
                print(train7.x)
                print(train7.y)
                print(player_x)
                print(player_y)
                run = False
    if train9 != 0:
        if train9.x - TRAIN_LENGTH < player_x and player_x < train9.x:
            if train9.y < player_y and player_y < train9.y + TRAIN_HEIGHT:
                print('9')
                print(train9.x)
                print(train9.y)
                print(player_x)
                print(player_y)
                run = False
    pygame.display.update()

win = pygame.display.set_mode((500, 500))
endScreen = pygame.image.load("C:\\Users\\User\\PycharmProjects\\ROI-AND-EFRAT-PROJECT\\end.jpeg")
endScreen = pygame.transform.scale(endScreen, (500, 500))
win.blit(endScreen, (0, 0))
font_name = "Arial"
text_size = 40
text = str(timer)
color = (0, 0, 0)
font = pygame.font.SysFont(font_name, text_size)
win.blit(font.render(text, True, color), (310, 90))

pygame.display.update()

time.sleep(3)
