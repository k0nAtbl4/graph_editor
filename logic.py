import pygame

WIDTH = 1000
HEIGHT = 800
# Цвета
YELLOW_BG = (255, 255, 224)  # Светло-жёлтый (как тетрадный лист)
GRID_COLOR = (200, 200, 150)  # Тёмно-жёлтый для сетки
PLAYER_COLOR = (255, 0, 0)  # Красный игрок для наглядности

# Параметры сетки
CELL_SIZE = 40  # Размер клетки


def draw_grid(screen,camera_x,camera_y):
    """Рисует сетку с учётом смещения камеры"""
    # Вертикальные линии
    for x in range(-CELL_SIZE, WIDTH + CELL_SIZE, CELL_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (x - camera_x % CELL_SIZE, 0),
            (x - camera_x % CELL_SIZE, HEIGHT),
        )
    # Горизонтальные линии
    for y in range(-CELL_SIZE, HEIGHT + CELL_SIZE, CELL_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, y - camera_y % CELL_SIZE),
            (WIDTH, y - camera_y % CELL_SIZE),
        )

def draw_point(screen,x,y,r,color):
    pygame.draw.circle(screen, color, (x, y), r)