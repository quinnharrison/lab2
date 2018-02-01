#!/usr/bin/python

import pygame, sys
from pygame.locals import*

pygame.init()






while True:   #main game loop


  

  for event in pygame.event.get():
    


    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    pygame.display.update()
