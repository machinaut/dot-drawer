#!/usr/bin/env python
import pygame
pygame.init()

inch = 10
size = width, height = 48 * inch, 24 * inch

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
world = pygame.image.load('transformedworld.png')
worldrect = world.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(white)
    screen.blit(world, worldrect)
    pygame.display.flip()
