import pygame

def get_square_click(screen, square_size, margin_x, margin_y):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Проверка, находится ли клик внутри большого квадрата
                if mouse_x < margin_x or mouse_x > margin_x + square_size * 9:
                    print('mimo')
                    return None
                if mouse_y < margin_y or mouse_y > margin_y + square_size * 9:
                    print('mimo')
                    return None

                square_x = (mouse_x - margin_x - 1) // square_size
                square_y = (mouse_y - margin_y - 1) // square_size

                # print('клик по ', square_x, square_y)
                return (square_x, square_y)
