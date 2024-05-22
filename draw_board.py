import pygame

board_color = (128, 128, 128)
block_color = (0, 0, 0)
blue_color = (0, 0, 255)
white_color = (0, 0, 0)


def draw_board(board, margin, sq_size, screen):
    for i in range(0, 9):
        for j in range(0, 9):
            # Координаты маленького квадрата
            x = margin + i * sq_size
            y = j * sq_size  # Изменение здесь

            # Рисование квадрата
            if board[i][j] == 1:
                pygame.draw.rect(screen, blue_color, (x, y, sq_size, sq_size), 3)
            else:
                pygame.draw.rect(screen, white_color, (x, y, sq_size, sq_size), 3)
