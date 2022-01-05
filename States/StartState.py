from pygame.locals import *
import States.BaseState
import pygame

class StartState(States.BaseState.BaseState):
    def __init__(self):
        from main import WINDOW_HEIGHT, WINDOW_WIDTH, RESIZE_COEFFICIENT
        self.title = pygame.transform.scale(pygame.image.load('title.png'), (pygame.image.load('title.png').get_width() * RESIZE_COEFFICIENT, pygame.image.load('title.png').get_height() * RESIZE_COEFFICIENT))
        self.titleRect = self.title.get_rect()
        self.titleRect.center = (WINDOW_WIDTH / 2 , WINDOW_HEIGHT / 2 - 150 * RESIZE_COEFFICIENT)
        self.titleRect.size

    def update(self):
        from main import gStateMachine
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER]:
            gStateMachine.change("Play", None)

    def render(self):
        from main import DISPLAYSERF
        DISPLAYSERF.blit(self.title, self.titleRect)
    