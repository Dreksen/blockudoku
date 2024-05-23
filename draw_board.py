import pygame

BORDER_WIDTH = 5
# board_color = (128, 128, 128)
border_color = (0, 0, 0)
blue_color = (0, 0, 255)
white_color = (255, 255, 255)
grey_color = (200, 200, 200)
grey_blocks = [[0, 1], [1, 0], [1, 2], [2, 1]]


def draw_board(board, Screen, screen):
    for box_x in range(3):
        for box_y in range(3):
            for i in range(3):
                for j in range(3):
                    # Координаты маленького квадрата
                    block = [box_x * 3 + i, box_y * 3 + j]
                    x = Screen.margin_x + block[0] * Screen.sq_size
                    y = Screen.margin_y + block[1] * Screen.sq_size  # Изменение здесь

                    # Рисование квадрата
                    if board[block[0]][block[1]] == 1:
                        pygame.draw.rect(screen, blue_color, (x, y, Screen.sq_size, Screen.sq_size))
                    else:
                        if [box_x, box_y] in grey_blocks:
                            pygame.draw.rect(screen, grey_color, (x, y, Screen.sq_size, Screen.sq_size))
                        else:
                            pygame.draw.rect(screen, white_color, (x, y, Screen.sq_size, Screen.sq_size))
                    pygame.draw.rect(screen, border_color, (x, y, Screen.sq_size, Screen.sq_size), 3)

