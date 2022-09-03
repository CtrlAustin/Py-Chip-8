import math

import pygame

print("hello world")
pygame.init()

cols = 64
rows = 32

scaling_factor = 4

screen_width = cols * scaling_factor
screen_height = rows * scaling_factor

pixel_width = 1 * scaling_factor
pixel_height = 1 * scaling_factor

black = (0, 0, 0)
white = (255, 255, 255)
win = pygame.display.set_mode((screen_width * scaling_factor, screen_height * scaling_factor))

screen = pygame.Surface((screen_width, screen_height))
display = pygame.display.set_mode((cols*scaling_factor, rows*scaling_factor *2))

screen_contents = [0 * cols] * rows

pixel = pygame.Rect(win.get_rect().center, (0, 0)).inflate(*([min(win.get_size()) // 2] * 2))

color = white


def init():
    clear()
    main()


def main():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        testdraw()
        renderer()
    pass


def renderer():
    clear()

    for i in screen_contents:
        #result = screen_contents[i] % cols
        x = (i % cols) * scaling_factor
        y = math.floor(i / cols) * scaling_factor
        # u = x / (screen_width - 1)
        # color = (round(u * 255), 0, round((1 - u) * 255))
        if screen_contents[i == 1]:
            pygame.draw.rect(display, color, (pixel.left + x * scaling_factor * 2, pixel.top + y * scaling_factor, pixel_width, pixel_height))
    pygame.display.update()


def setpixel(x, y):
    if x > cols:
        x = x - cols
    if x < 0:
        x = x + cols

    if y > rows:
        y = y - rows
    if y < 0:
        y = y + rows

    pixelloc = x
    print(pixelloc)
    # for i in screen_contents:
    #if screen_contents[pixelloc] == 0:  # toggles between erase (0) and draw (1)
    screen_contents[pixelloc] = 0 if True else 1
    return pixelloc


def clear():
    screen.fill(black)
    screen_contents = [cols * rows]
    for x in range(rows):
        for y in range(cols):
            pygame.draw.rect(display, black, (pixel.left + (x + .5) * scaling_factor * 2, pixel.top + y * scaling_factor, pixel_width, pixel_height))


def testdraw():
    setpixel(1, 0)
    setpixel(2, 0)
    setpixel(3, 0)



init()
