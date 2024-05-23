import pygame
def points_show(screen, points):
    x, y = 5, 5
    TEXT_COLOR = (0, 0, 0)
    FONT = pygame.font.SysFont("Arial", 25)
    TEXT = f'Points: {points}'
    text_object = FONT.render(TEXT, True, TEXT_COLOR)
    screen.blit(text_object, (x, y))

def game_over_show(screen, points):
    x, y = 5, 5
    TEXT_COLOR = (0, 0, 0)
    FONT = pygame.font.SysFont("Arial", 25)
    TEXT = f'Game over. You got {points} points'
    text_object = FONT.render(TEXT, True, TEXT_COLOR)
    screen.blit(text_object, (x, y))