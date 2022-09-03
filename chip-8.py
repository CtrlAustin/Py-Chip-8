import time
import pygame
import renderer2 as renderer
import input

pygame.init()

fps = 60

run = True
fpsInterval = 1000 / fps;
then = time.time()


def init():
    then = time.time()
    startTime = then

    # TESTING CODE. REMOVE WHEN DONE TESTING.
    renderer.testdraw()
    renderer.render()
    # END TESTING CODE
    time.sleep(.5)
    main()


def main():
    while run:
        step()


def step():
    now = time.time()
    elapsed = now - then
    # if elapsed > fpsInterval:
        # Cycle the CPU. We'll come back to this later and fill it out.


init()

