import pygame
from graphs import BinaryTree
from logic import *
from consts import *

# Инициализация Pygame
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("joystick sodaluv uwu")


myscreen = MyScreen(WIDTH, HEIGHT, [], 0, 0, screen)

start_mouse = (0, 0)
curr_mouse = (0, 0)
last_mouse = (0, 0)
new_mouse = (0, 0)
running = True
is_pressed = False
is_start = True

entities = [] #[Tree]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_pressed = True
            is_start = True
        if event.type == pygame.MOUSEBUTTONUP:
            is_pressed = False
    if is_pressed == True:
        if is_start == False:
            last_mouse = curr_mouse
        is_start = False
        curr_mouse = pygame.mouse.get_pos()
        if curr_mouse != last_mouse:
            myscreen.x += last_mouse[0] - curr_mouse[0]
            myscreen.y += last_mouse[1] - curr_mouse[1]
    screen.fill(BACK_COLOR)
    myscreen.draw_greed(100)
    pygame.display.flip()

# Выход из Pygame
pygame.quit()


# pygame.draw.lines(screen, GREY, True, [(0, 0), (500, 200),(0, 0), (700, 400)], 5)
