import time

import pygame
import math
pygame.init()

cols = 65
rows = 33

scaling_factor = 20

black = (0, 0, 0)
white = (255, 255, 255)

win = pygame.display.set_mode((cols * scaling_factor, rows * scaling_factor))

screen_contents = [0] * (cols * rows)

display = pygame.display.set_mode((cols * scaling_factor, rows * scaling_factor))


def render():
    clear()
    for i, value in enumerate(screen_contents):
        if value == 1:
            pixelX = i % cols
            pixelY = math.floor(i / cols)
            pygame.draw.rect(display, white, (pixelX * scaling_factor, pixelY * scaling_factor, scaling_factor, scaling_factor))
            pygame.display.update()


def setpixel(x, y):
    pixelloc = (y * cols) + x
    # print(pixelloc)
    screen_contents[pixelloc] = 1


def clear():
    for i in screen_contents:
        i = 0
    display.fill((0, 0, 0))


# demo draws
def testdraw():
    setpixel(3, 3)
    setpixel(2, 5)
    setpixel(3, 0)
    setpixel(12, 20)
    setpixel(13, 20)
    setpixel(14, 20)
    setpixel(15, 20)
    setpixel(12, 21)
    setpixel(13, 22)
    setpixel(14, 23)
    setpixel(15, 24)
    setpixel(64, 32)


def checkers():
    clear()