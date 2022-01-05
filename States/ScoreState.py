import States.BaseState
import pygame
from pygame.locals import *

class ScoreState(States.BaseState.BaseState):
    def __init__(self):
        pass
    def enter(self, params):
        self.score = params
    def update(self):
        from main import DISPLAYSERF, WHITE, WINDOW_HEIGHT, WINDOW_WIDTH, RESIZE_COEFFICIENT
        pygame.init()
        font = pygame.font.Font('freesansbold.ttf', 64)
        text = pygame.transform.scale(font.render('You Crashed', True, WHITE), (font.render('You Crashed', True, WHITE).get_width() * RESIZE_COEFFICIENT, font.render('You Crashed', True, WHITE).get_height() * RESIZE_COEFFICIENT))
        text1 = pygame.transform.scale(font.render(f"Score: {self.score}", True, WHITE), (font.render(f"Score: {self.score}", True, WHITE).get_width() * RESIZE_COEFFICIENT, font.render(f"Score: {self.score}", True, WHITE).get_height() * RESIZE_COEFFICIENT))
        textRect = text.get_rect()
        text1Rect = text1.get_rect()
        textRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 150 * RESIZE_COEFFICIENT)
        text1Rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 70 * RESIZE_COEFFICIENT)
        DISPLAYSERF.blit(text, textRect)
        DISPLAYSERF.blit(text1, text1Rect)

        pressed_keys = pygame.key.get_pressed()

        from main import gStateMachine
        if pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER]:
            gStateMachine.change("Play", None)

    def render(self):
        pass