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
from points_show import *

pygame.init()


class Screen:
    screen_width = 500
    screen_height = 600
    sq_size = 40
    margin_x = (screen_width - (9 * sq_size)) // 2
    margin_y = 40
    sq_width = 9 * sq_size

screen = pygame.display.set_mode((Screen.screen_width,Screen.screen_height))
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
    [(0, 0), (0, -1), (1, -1), (2, -1)],  # неполный угол 10-11
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



def award_points(blocks, parts):
    return parts * 9


current_points = 0
draw_board(board, Screen, screen)
points_show(screen, current_points)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    block = random.choice(blocks)

    screen.fill((255, 255, 255))
    draw_board(board, Screen, screen)
    draw_next_block(block, screen, Screen)

    if is_board_complete(board, block):
        print("GAME OVER")
        game_over_show(screen, current_points)
        pygame.display.update()
        time.sleep(1000)
    points_show(screen, current_points)
    pygame.display.update()

    position = get_square_click(screen, Screen)
    while is_valid_move(board, block, position) is False:
        print("Невозможно поместить блок в эту позицию.")
        position = get_square_click(screen, Screen)

    place_block(board, block, position)
    draw_board(board, Screen, screen)
    pygame.display.update()
    # print(board)

    matching_rows_cols_blocks = find_matching_rows_and_cols_and_blocks(board)
    got_award_points = 0
    if matching_rows_cols_blocks != ([], [], []):
        blocks_disappeared, parts = reset_matching_rows_and_cols_and_blocks(board, matching_rows_cols_blocks[0],
                                                                matching_rows_cols_blocks[1],
                                                                matching_rows_cols_blocks[2])
        got_award_points = award_points(blocks_disappeared, parts)
        print(f"Исчезло {parts} рядов/столбцов! Вы получили {got_award_points} очков.")
    got_award_points += len(block)
    current_points += got_award_points
    draw_board(board, Screen, screen)
    points_show(screen, current_points)
    pygame.display.update()

    pygame.display.update()
