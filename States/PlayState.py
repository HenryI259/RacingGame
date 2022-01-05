import States.BaseState
import pygame
from enemy import Enemy
import random

class PlayState(States.BaseState.BaseState):
    def enter(self, params):
        from main import player
        self.enemyList = []
        self.updateTimer = 0
        self.spawnSpeed = 90
        self.score = 0
        player.x, player.y = 600, 600

    def update(self):
        from main import RESIZE_COEFFICIENT
        self.updateTimer += 1
        if self.updateTimer % 5 == 0 and self.spawnSpeed > 60:
            self.spawnSpeed -= 1
        
        if self.updateTimer % self.spawnSpeed == 0:
            randomType = random.randint(1, 4)
            if randomType == 1 or randomType == 2:
                enemyType = 1
            elif randomType == 3:
                enemyType = 2
            elif randomType == 4:
                enemyType = 3

            from main import Background, WINDOW_HEIGHT, WINDOW_WIDTH
            if enemyType != 2:
                enemyY = random.randint(int(Background.rect.height), int(WINDOW_HEIGHT) - int(90 * RESIZE_COEFFICIENT)) / RESIZE_COEFFICIENT
            else:
                enemyY = random.randint(int(Background.rect.height) + int(90 * RESIZE_COEFFICIENT), int(WINDOW_HEIGHT) - int(180 * RESIZE_COEFFICIENT)) / RESIZE_COEFFICIENT

            self.enemyList.append(Enemy(WINDOW_WIDTH / RESIZE_COEFFICIENT, enemyY, "enemy.png", random.randint(10, 20), enemyType))
        
        from main import gStateMachine, collidCheck, player, RESIZE_COEFFICIENT
        for enemy in self.enemyList:
            enemy.update()
            if collidCheck(player, enemy):
                gStateMachine.change("Score", self.score)
            if enemy.x < -enemy.width:
                self.enemyList.remove(enemy)
                self.score += 1

        from main import player
        player.update()

    def render(self):
        from main import player

        for enemy in self.enemyList:
            enemy.render()

        player.render()
        
        from main import WHITE, DISPLAYSERF, RESIZE_COEFFICIENT
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = pygame.transform.scale(font.render(f"Score: {self.score}", True, WHITE), (font.render(f"Score: {self.score}", True, WHITE).get_width() * RESIZE_COEFFICIENT, font.render(f"Score: {self.score}", True, WHITE).get_height() * RESIZE_COEFFICIENT))
      
        textRect = text.get_rect()
        textRect.center = (50 * RESIZE_COEFFICIENT, 15 * RESIZE_COEFFICIENT)
        DISPLAYSERF.blit(text, textRect)

    