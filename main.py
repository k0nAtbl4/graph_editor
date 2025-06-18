import pygame
from graphs import BinaryTree
from logic import *

WIDTH = 1000
HEIGHT = 800
FPS = 10000
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ЕГОРУШКА")
clock = pygame.time.Clock()
camera_x = 0
camera_y = 0
running = True
YELLOW_BG = (255, 255, 224)
BLACK = (0,0,0)


screen.fill(YELLOW_BG)

pressed=True
draw_grid(screen=screen, camera_x=camera_x, camera_y=camera_y)
pygame.display.flip()
while running:
    # Держим цикл на правильной скорости
    # clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pressed=(True)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed=(False)
        if pressed==False:
            x, y = pygame.mouse.get_pos()
            draw_point(screen=screen,x=x,y=y,color=BLACK,r=2)
    if pressed==False:
        x, y = pygame.mouse.get_pos()
        draw_point(screen=screen,x=x,y=y,color=BLACK,r=2)
    pygame.display.flip()