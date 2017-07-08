import pygame
import sys
from random import randint
import time
from pygame.locals import *
import math

pygame.init()
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
NUMBER_OF_BALLS = 200
BLACK = (0, 0, 0)
GRAVITY = (math.pi, 0.5)
DRAG = 0.9999
ELASTICITY = 0.9
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Balls')

balls = []
for i in range(NUMBER_OF_BALLS):
    ball = {
        'x': randint(100, 300),
        'y': randint(100, 300),
        'radius': 10,
        'color': (randint(0, 255), randint(0, 255), randint(0, 255)),
        'speed': randint(5, 10),
        'angle': (math.pi / 32) * randint(0, 32)
    }
    balls.append(ball)


def add_vectors(angle1, length1, angle2, length2):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    length = math.hypot(x, y)
    angle = 0.5 * math.pi - math.atan2(y, x)
    return (angle, length)


def move(ball):
    ball['x'] += math.sin(ball['angle']) * ball['speed']
    ball['y'] -= math.cos(ball['angle']) * ball['speed']

    if ball['x'] - ball['radius'] < 0 or ball['x'] + ball['radius'] > WINDOWWIDTH:
        ball['angle'] = 2 * math.pi - ball['angle']
        ball['x'] = min(max(ball['x'], ball['radius']), WINDOWWIDTH - ball['radius'])
        ball['speed'] *= ELASTICITY

    if ball['y'] - ball['radius'] < 0 or ball['y'] + ball['radius'] > WINDOWHEIGHT:
        ball['angle'] = math.pi - ball['angle']
        ball['y'] = min(max(ball['y'], ball['radius']), WINDOWHEIGHT - ball['radius'])
        ball['speed'] *= ELASTICITY

    (ball['angle'], ball['speed']) = add_vectors(ball['angle'], ball['speed'], GRAVITY[0], GRAVITY[1])
    ball['speed'] *= DRAG


def collide(ball1, ball2):
    dx = ball1['x'] - ball2['x']
    dy = ball1['y'] - ball2['y']
    distance = math.hypot(dx, dy)
    if distance < ball1['radius'] + ball2['radius']:
        tangent = math.atan2(dy, dx)
        ball1['angle'] = 2 * tangent - ball1['angle']
        ball2['angle'] = 2 * tangent - ball2['angle']
        (ball1['speed'], ball2['speed']) = (ball2['speed'], ball1['speed'])
        ball1['speed'] *= ELASTICITY
        ball2['speed'] *= ELASTICITY
        overlap = ball1['radius'] + ball2['radius'] - distance
        angle = 0.5 * math.pi + tangent
        ball1['x'] += (math.sin(angle) * 0.5 * overlap)
        ball1['y'] -= (math.cos(angle) * 0.5 * overlap)
        ball2['x'] -= (math.sin(angle) * 0.5 * overlap)
        ball2['y'] += (math.cos(angle) * 0.5 * overlap)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(BLACK)

    for i, ball in enumerate(balls):
        before = ball['speed']
        move(ball)
        if ball['speed'] > before:
            print('speed increased', before, ball['speed'])
        for other_ball in balls[i + 1:]:
            collide(ball, other_ball)
        pygame.draw.circle(windowSurface, ball['color'], (int(ball['x']), int(ball['y'])), ball['radius'])

    pygame.display.update()
    time.sleep(0.02)
