import pygame
import sys
from random import randint
import time
from pygame.locals import *

pygame.init()
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Balls')

DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
DIRECTIONS = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

MOVESPEED = 4

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

NUMBER_OF_BALLS = 100

balls = []
for i in range(NUMBER_OF_BALLS):
    ball = {
        'x': randint(0, 200),
        'y': randint(0, 200),
        'radius': randint(0, 50),
        'color': (randint(0, 255), randint(0, 255), randint(0, 255)),
        'dir': DIRECTIONS[randint(0, 3)]
    }
    balls.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(BLACK)

    for b in balls:
        if b['dir'] == DOWNLEFT:
            b['x'] -= MOVESPEED
            b['y'] += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['x'] += MOVESPEED
            b['y'] += MOVESPEED
        if b['dir'] == UPLEFT:
            b['x'] -= MOVESPEED
            b['y'] -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['x'] += MOVESPEED
            b['y'] -= MOVESPEED

        if b['y'] - b['radius'] < 0:
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['y'] + b['radius'] > WINDOWHEIGHT:
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['x'] - b['radius'] < 0:
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['x'] + b['radius'] > WINDOWWIDTH:
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
        pygame.draw.circle(windowSurface, b['color'], (b['x'], b['y']), b['radius'])

    pygame.display.update()
    time.sleep(0.02)
