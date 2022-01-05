from entity import Entity
import pygame

class Enemy(Entity):
    def __init__(self, x, y, sprite, speed, type):
        super().__init__(x, y, sprite)
        self.speed = speed
        self.type = type
        self.updateTimer = 0
    def update(self):
        from main import player
        self.updateTimer += 1
        self.x -= self.speed

        if self.type == 2:
            if ((self.updateTimer % 60) - 30) > 0:
                self.y += 3
            elif ((self.updateTimer % 60) - 30) < 0:
                self.y -= 3
        if self.type == 3:
            if self.updateTimer % 1 == 0:
                if player.y - self.y > 0:
                    self.y += 2
                elif player.y - self.y < 0:
                    self.y -= 2

        return super().update()