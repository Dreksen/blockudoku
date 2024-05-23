import random
import sys
import time
import numpy as np
import pygame
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
    [(0, 0)],  # 1x1
    [(0, 0), (0, -1)],  # 1x2
    [(0, 0), (1, 0)],  # 2x1
    [(0, 0), (0, -1), (1, 0)],  # угол 7-8
    [(0, 0), (0, -1), (1, -1)],  # угол 10-11
    [(0, 0), (1, 0), (1, -1)],  # угол 4-5
    [(0, 0), (1, 0), (1, 1)],  # угол 2-3
    [(0, 0), (1, 0), (2, 0)],  # Прямоугольник 3x1
    [(0, 0), (0, -1), (0, -2)],  # Прямоугольник 1x3
    [(0, 0), (0, -1), (1, 0), (1, -1)],  # квадрат

    [(0, 0), (0, -1), (0, -2), (1, 0)],  # неполнлый угол 7-8
    [(0, 0), (0, -1), (1, 0), (2, 0)],  # неполный угол 7-8
    [(0, 0), (0, -1), (1, -2), (2, -2)],  # неполный угол 10-11
    [(0, 0), (0, -1), (0, -2), (1, -2)],  # неполный угол 10-11
    [(0, 0), (1, 0), (1, -1), (1, -2)],  # неполный угол 4-5
    [(0, 0), (1, 0), (2, 0), (2, -1)],  # неполный угол 4-5
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # неполный угол 2-3
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # неполный угол 2-3

    [(0, 0), (0, -1), (0, -2), (1, 0), (2, 0)],  # угол 7-8
    [(0, 0), (0, -1), (0, -2), (1, -2), (2, -2)],  # угол 10-11
    [(0, 0), (1, 0), (2, 0), (2, -1), (2, -2)],  # угол 4-5
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # угол 2-3
]



sq_size = 40
margin_x = (screen_width - (9 * sq_size)) // 2
margin_y = 0
sq_width = 9 * sq_size

def award_points(num_disappeared):
    points = num_disappeared * 100
    return points

draw_board(board, margin_x, margin_y, sq_size, screen)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    block = random.choice(blocks)

    screen.fill((255, 255, 255))
    draw_board(board, margin_x, margin_y, sq_size, screen)
    draw_next_block(block, screen, screen_width, screen_height)
    pygame.display.update()

    if is_board_complete(board, block):
        print("GAME OVER")
        time.sleep(1000)

    position = get_square_click(screen, sq_size, margin_x, margin_y)
    while is_valid_move(board, block, position) is False:
        print("Невозможно поместить блок в эту позицию.")
        position = get_square_click(screen, sq_size, margin_x, margin_y)

    place_block(board, block, position)
    draw_board(board, margin_x, margin_y, sq_size, screen)
    pygame.display.update()

    matching_rows_cols_blocks = find_matching_rows_and_cols_and_blocks(board)
    if matching_rows_cols_blocks != ([],[], []):
        print(matching_rows_cols_blocks)
        reset_matching_rows_and_cols_and_blocks(board, matching_rows_cols_blocks[0], matching_rows_cols_blocks[1], matching_rows_cols_blocks[2])
        draw_board(board, margin_x, margin_y, sq_size, screen)
        pygame.display.update()
        points = award_points(num_disappeared)
        print(f"Исчезло {num_disappeared} рядов/столбцов! Вы получили {points} очков.")

    pygame.display.update()
