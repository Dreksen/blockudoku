import random
import sys
import time
import numpy as np
import pygame
from check_for_disappeared import *
from draw_board import *
from get_click_pos import *
from is_valid_move import *
from place_block import *
from draw_next_block import *
from is_board_complete import *
from delete_disappeared import *

pygame.init()
screen_width = 500
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))  # Белый

# Определить цвета
board_color = (128, 128, 128)
block_color = (0, 0, 0)
blue_color = (0, 0, 255)
white_color = (0, 0, 0)
num_disappeared = 10

# Создать двумерный массив для представления доски

board = np.zeros((9, 9), dtype=int)

# Создать список блоков разных форм и размеров
blocks = [
    [(0, 0), (0, -1), (1, 0)],  # угол 7-8
    [(0, 0), (0, -1), (0, -2)],  # Прямоугольник 1x3
    [(0, 0), (1, 0), (2, 0)],  # Прямоугольник 3x1
    [(0, 0), (0, -1), (1, -1)],  # угол 10-11
    [(0, 0), (1, 0), (1, -1)],  # угол 4-5
    [(0, 0), (1, 0), (1, 1)],  # угол 2-3
    [(0, 0), (0, -1), (1, 0), (1, -1)],  # квадрат
]


def award_points(num_disappeared):
    points = num_disappeared * 100
    return points


# Размеры квадрата
sq_size = 40
margin = (screen_width - (9 * sq_size)) // 2
sq_width = 9 * sq_size

# def draw_board(board):
    # # Определить цвета
    # board_color = (255, 255, 255)  # Белый
    # line_color = (0, 0, 0)  # Черный
    #
    # # Нарисовать линии сетки
    # for i in range(11):
    #     # Горизонтальные линии
    #     pygame.draw.line(screen, line_color, (60*i, 0), (60*i, screen_height))
    #     # Вертикальные линии
    #     pygame.draw.line(screen, line_color, (0, 60*i), (screen_width, 60*i))
    #
    # # Нарисовать квадрат вокруг линий сетки
    # pygame.draw.rect(screen, line_color, (0, 0, screen_width, screen_height), 3)
    #
    # # Закрасить все, что находится за пределами квадрата, в белый цвет
    # pygame.draw.rect(screen, board_color, (0, 0, screen_width, 60))
    # pygame.draw.rect(screen, board_color, (0, screen_height-60, screen_width, 60))
    # pygame.draw.rect(screen, board_color, (0, 60, 60, screen_height-120))
    # pygame.draw.rect(screen, board_color, (screen_width-60, 60, 60, screen_height-120))

    # for i in range(0, 9):
    #     for j in range(0, 9):
    #         # Координаты маленького квадрата
    #         x = MARGIN + i * SQUARE_SIZE
    #         y = (SCREEN_HEIGHT - SQUARE_WIDTH) // 2 + j * SQUARE_SIZE
    #
    #         # Рисование квадрата
    #         pygame.draw.rect(screen, (0, 0, 0), (x, y, SQUARE_SIZE, SQUARE_SIZE), 1)




draw_board(board, margin, sq_size, screen)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    block = random.choice(blocks)
    screen.fill((255, 255, 255))
    draw_board(board, margin, sq_size, screen)
    draw_next_block(block, screen, screen_width, screen_height)
    pygame.display.update()
    if is_board_complete(board, block):
        print("GAME OVER")
        time.sleep(1000)

    position = get_square_click(screen, sq_size, margin)
    while is_valid_move(board, block, position) is False:
        print("Невозможно поместить блок в эту позицию.")
        position = get_square_click(screen, sq_size, margin)

    # Поместить блок на доску
    place_block(board, block, position)
    print(board)
    draw_board(board, margin, sq_size, screen)
    pygame.display.update()

    matching_rows_and_cols = find_matching_rows_and_cols(board)
    if matching_rows_and_cols:
        # Наградить игрока очками
        reset_matching_rows_and_cols(board, matching_rows_and_cols[0], matching_rows_and_cols[1])
        draw_board(board, margin, sq_size, screen)
        pygame.display.update()
        points = award_points(num_disappeared)
        print(f"Исчезло {num_disappeared} рядов/столбцов! Вы получили {points} очков.")

    # clock.tick(FPS)
    pygame.display.update()
