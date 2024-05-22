import pygame

def get_square_click(screen, square_size, margin):
    # Получение координат клика мыши
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Проверка, находится ли клик внутри большого квадрата
                if mouse_x < margin or mouse_x > margin + square_size * 9:
                    print('mimo')
                    return None
                if mouse_y > square_size * 9:
                    print('mimo')
                    return None

                # Вычисление координат квадрата, по которому был сделан клик
                square_x = (mouse_x - margin - 1) // square_size
                square_y = (mouse_y - 1) // square_size

                # Возврат координат квадрата
                print('клик по ', square_x, square_y)
                return (square_x, square_y)
