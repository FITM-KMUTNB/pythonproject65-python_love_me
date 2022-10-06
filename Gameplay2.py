import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)