import pygame
from entity import Entity
from pygame import *


class Car(Entity):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
    
    def update(self):
        super().update()

        from main import WINDOW_WIDTH, WINDOW_HEIGHT, Background, RESIZE_COEFFICIENT
        
        pressed_keys = pygame.key.get_pressed()

        if self.rect.x > 0:
            if pressed_keys[K_LEFT]:
                self.x -= 8
        if self.rect.x < WINDOW_WIDTH - self.width:       
            if pressed_keys[K_RIGHT]:
                self.x += 8
        if self.rect.y > Background.rect.height:
            if pressed_keys[K_UP]:
                self.y -= 8
        if self.rect.y < WINDOW_HEIGHT - self.height - 45 * RESIZE_COEFFICIENT:
            if pressed_keys[K_DOWN]:
                self.y += 8