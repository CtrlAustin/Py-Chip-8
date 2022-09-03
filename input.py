import pygame

# define the keymap

keyspressed = []
keymap = ["1", "2", "3", "C", "4", "5", "6", "D", "7", "8", "9", "E", "A", "0", "B", "F"]


def pressed(keycode):
    for event in pygame.event.get():
        keyspressed.append(event.key)
        for i in keyspressed:
            print(i)


def keydown():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("up")


def keyup():
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            print("down")
