import pygame
def draw_next_block(block, screen, Screen):
    # Определить цвета для блоков
    black_color = (0, 0, 0)  # Черный
    blue_color = (100, 100, 250)
    # Определить позицию следующего блока
    x = Screen.screen_width // 2 - 30
    y = Screen.screen_height - 120

    for x_offset, y_offset in block:
        pygame.draw.rect(screen, blue_color, (x + x_offset*30, y + y_offset*30, 30, 30))
        pygame.draw.rect(screen, black_color, (x + x_offset*30, y + y_offset*30, 30, 30), 3)


