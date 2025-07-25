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
        left=BinaryTree(2, left=None, right=None, coordinate=(-20, -100)),
        right=BinaryTree(3, left=None, right=None, coordinate=(40, -100)),
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
            myscreen.x += last_mouse[0] - curr_mouse[0]
            myscreen.y += last_mouse[1] - curr_mouse[1]
            # last_pos = new_pos
            # new_pos = (myscreen.x, myscreen.y)
    screen.fill(BACK_COLOR)
    myscreen.draw_greed(100)
    text = font.render(f'{myscreen.x}{myscreen.y}  |  {is_pressed}', True, (255,255,255))
    
    # Позиция текста (левый верхний угол)
    screen.blit(text, (10, 10))  # Отступ 10 пикселей от края
    # if is_pressed == False:
    myscreen.draw_Trees(500, 400, entities)
    pygame.display.flip()

# Выход из Pygame
pygame.quit()


# pygame.draw.lines(screen, GREY, True, [(0, 0), (500, 200),(0, 0), (700, 400)], 5)
