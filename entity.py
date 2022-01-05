import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite):
        from main import RESIZE_COEFFICIENT
        super().__init__()
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(pygame.image.load(sprite), (pygame.image.load(sprite).get_width() * RESIZE_COEFFICIENT, pygame.image.load(sprite).get_height() * RESIZE_COEFFICIENT))
        self.rect = self.sprite.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.hitboxes = False
    def update(self):
        from main import RESIZE_COEFFICIENT
        self.rect.x = self.x * RESIZE_COEFFICIENT
        self.rect.y = self.y * RESIZE_COEFFICIENT
    def render(self):
        from main import DISPLAYSERF, RED
        DISPLAYSERF.blit(self.sprite, self.rect)
        if self.hitboxes:
            pygame.draw.rect(DISPLAYSERF, RED, self.rect, 1)
    def collide(self, other):
        pass