
import pygame
import sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption("Hola Mundo!")

while True: # main game

    for event in pygame.event.get():
        if event.type == QUIT:

         pygame.quit()

         sys.exit()

    pygame.display.update()
