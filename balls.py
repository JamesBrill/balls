import pygame
import sys
from random import randint
import time
from pygame.locals import *
import math

pygame.init()
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
NUMBER_OF_BALLS = 100
BLACK = (0, 0, 0)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Balls')

balls = []
for i in range(NUMBER_OF_BALLS):
    ball = {
        'x': randint(100, 200),
        'y': randint(100, 200),
        'radius': randint(10, 50),
        'color': (randint(0, 255), randint(0, 255), randint(0, 255)),
        'speed': randint(5, 10),
        'angle': (math.pi / 32) * randint(0, 32)
    }
    balls.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(BLACK)

    for ball in balls:
        ball['x'] += math.sin(ball['angle']) * ball['speed']
        ball['y'] -= math.cos(ball['angle']) * ball['speed']

        if ball['x'] - ball['radius'] < 0 or ball['x'] + ball['radius'] > WINDOWWIDTH:
            ball['angle'] = 2 * math.pi - ball['angle']

        if ball['y'] - ball['radius'] < 0 or ball['y'] + ball['radius'] > WINDOWHEIGHT:
            ball['angle'] = math.pi - ball['angle']

        pygame.draw.circle(windowSurface, ball['color'], (int(ball['x']), int(ball['y'])), ball['radius'])

    pygame.display.update()
    time.sleep(0.02)
