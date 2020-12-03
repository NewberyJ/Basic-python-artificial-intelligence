import pygame
from pygame.locals import *
from moviepy.editor import *
import subprocess


pygame.init()
screen = pygame.display.set_mode((455, 262))
pygame.display.set_caption('Jarvis')

clip = VideoFileClip('jarvis.mp4')

running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0
    else:
      print(event)

  screen.fill((0, 0, 0))
  clip.preview()
  pygame.display.flip()

pygame.quit()




