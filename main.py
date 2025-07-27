import pygame
from graphs import BinaryTree
from logic import *
from consts import *

# Инициализация Pygame
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("joystick sodaluv uwu")


myscreen = MyScreen(WIDTH, HEIGHT, [], 0, 0, screen)

last_pos = (0, 0)
curr_mouse = (0, 0)
last_mouse = (0, 0)
new_pos = (0, 0)
running = True
is_pressed = False
is_start = True
data_Tree = [
    BinaryTree(
        1,
        left=BinaryTree(2, left=None, right=None, coordinate=(-200, -700)),
        right=BinaryTree(3, left=None, right=None, coordinate=(200, -700)),
        coordinate=(0, 0),
    ),
]
font = pygame.font.SysFont("Arial", 50)

entities = []  # [Tree]
entities = BinaryTree.bfs(data_Tree[0])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_pressed = True
            last_mouse = pygame.mouse.get_pos()
            curr_mouse = pygame.mouse.get_pos()
            is_start = True
        if event.type == pygame.MOUSEBUTTONUP:
            is_pressed = False
            is_start = False

    if is_pressed == True:
        if is_start == False:
            last_mouse = curr_mouse
        is_start = False
        curr_mouse = pygame.mouse.get_pos()
        if curr_mouse != last_mouse:
            myscreen.x += (last_mouse[0] - curr_mouse[0])
            myscreen.y += (last_mouse[1] - curr_mouse[1])

    screen.fill(BACK_COLOR)
    myscreen.draw_greed(100)

    myscreen.draw_Trees(entities)




    text = font.render(
        f"{myscreen.x}{myscreen.y}  |  {is_pressed}", True, (255, 255, 255)
    )
    screen.blit(text, (10, 10))
    pygame.display.flip()

pygame.quit()
