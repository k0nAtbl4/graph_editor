import pygame
from consts import *


class MyScreen:
    def __init__(self, width, height, map_data, x, y, pygame_screen):
        self.width = width
        self.height = height
        self.map_data = map_data
        self.x = x
        self.y = y
        self.pygame_screen = pygame_screen

    def draw_greed(self, scale):  # scale = each N lines
        w_count = WIDTH // LINE_SIZE  # count of lines in width
        h_count = HEIGHT // LINE_SIZE  # count of lines in height
        start = (self.x - WIDTH // 2, self.y - HEIGHT // 2)  # start_x  start_y
        end = (self.x + WIDTH // 2, self.y + HEIGHT // 2)  # end_x  end_y
        draw_x = 0
        draw_y = 0
        for i in range(start[0], end[0]):
            if i % scale == 0:
                pygame.draw.line(
                    self.pygame_screen, GREY, (draw_x, 0), (draw_x, HEIGHT), LINE_SIZE
                )
            draw_x += 1
        for i in range(start[1], end[1]):
            if i % scale == 0:
                pygame.draw.line(
                    self.pygame_screen, GREY, (0, draw_y), (WIDTH, draw_y), LINE_SIZE
                )
            draw_y += 1

    def check_collision(self, rect_x, rect_y, rect_width, rect_height, circle_x, circle_y, circle_radius):
        # Находим ближайшую точку на прямоугольнике к центру окружности
        closest_x = max(rect_x, min(circle_x, rect_x + rect_width))
        closest_y = max(rect_y, min(circle_y, rect_y + rect_height))

        # Вычисляем расстояние между центром окружности и этой ближайшей точкой
        distance_x = circle_x - closest_x
        distance_y = circle_y - closest_y
        distance_squared = (distance_x * distance_x) + (distance_y * distance_y)

        # Если расстояние меньше радиуса окружности, они пересекаются
        return distance_squared < (circle_radius * circle_radius)

    def draw_Trees(self, x, y, data):  # data:  [Tree]
        # pygame.draw.circle(self.pygame_screen,(255,123,242),(x,y),150,30)
        for i in data:
            circle=i[1]
            if MyScreen.check_collision(self, x, y, WIDTH,HEIGHT,circle[0],circle[1],150):
                nx = circle[0]+self.x
                ny = circle[1]+self.y
                pygame.draw.circle(self.pygame_screen, (0,0,0), (nx,ny), 150, 30)
