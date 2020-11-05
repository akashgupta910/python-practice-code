import pygame
from pygame import display,movie
pygame.init()
screen = pygame.display.set_mode((1024, 768))
background = pygame.Surface((1024, 768))

screen.blit(background, (0, 0))
pygame.display.update()

movie = pygame.movie.Movie('C:\Python27\1.mpg')
mrect = pygame.Rect(0,0,140,113)
movie.set_display(screen, mrect.move(65, 150))
movie.set_volume(0)
movie.play()