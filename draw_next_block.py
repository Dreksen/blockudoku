import pygame
def draw_next_block(block, screen, screen_width, screen_height):
    # Определить цвета для блоков
    block_color = (0, 0, 0)  # Черный

    # Определить позицию следующего блока
    x = screen_width // 2 - 30
    y = screen_height - 120

    for x_offset, y_offset in block:
        pygame.draw.rect(screen, block_color, (x + x_offset*30, y + y_offset*30, 30, 30))
