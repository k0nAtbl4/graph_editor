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
            draw_x+=1
        for i in range(start[1], end[1]):
            if i % scale == 0:
                pygame.draw.line(
                    self.pygame_screen, GREY, (0, draw_y), (WIDTH, draw_y), LINE_SIZE
                )
            draw_y+=1

        # for i in range(0, w_count):
        #     x = i * scale
        #     pygame.draw.line(self.pygame_screen, GREY, (x, 0), (x, HEIGHT), LINE_SIZE)
        # for i in range(0, h_count):
        #     y = i * scale
        #     pygame.draw.line(self.pygame_screen, GREY, (0, y), (WIDTH, y), LINE_SIZE)
