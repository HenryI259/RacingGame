import pygame
import sys
import States.PlayState
import States.ScoreState
import States.StartState
import StateMachine
import car
from pygame.locals import *

#initalize pygame
pygame.init()

RESIZE_COEFFICIENT = 0.8

player = car.Car(600, 600, "car1.png")

FPS = 30
clock = pygame.time.Clock()

WINDOW_HEIGHT = 720 * RESIZE_COEFFICIENT
WINDOW_WIDTH = 1280 * RESIZE_COEFFICIENT

GROUND_SCROLL_SPEED = 15 * RESIZE_COEFFICIENT
BACKGROUND_SCROLL_SPEED = 3 * RESIZE_COEFFICIENT
LOOPING_POINT = 1280 * RESIZE_COEFFICIENT

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

Road = pygame.sprite.Sprite()
Road.image = pygame.transform.scale(
    pygame.image.load("road.png"),
    (pygame.image.load("road.png").get_width() * RESIZE_COEFFICIENT,
     pygame.image.load("road.png").get_height() * RESIZE_COEFFICIENT))
Road.rect = Road.image.get_rect()
Road.rect.topleft = (0 * RESIZE_COEFFICIENT, 0 * RESIZE_COEFFICIENT)

Background = pygame.sprite.Sprite()
Background.image = pygame.transform.scale(
    pygame.image.load("background.png"),
    (pygame.image.load("background.png").get_width() * RESIZE_COEFFICIENT,
     pygame.image.load("background.png").get_height() * RESIZE_COEFFICIENT))

Background.rect = Background.image.get_rect()
Background.rect.topleft = (0 * RESIZE_COEFFICIENT, 0 * RESIZE_COEFFICIENT)

groundScroll = 0 * RESIZE_COEFFICIENT
backgroundScroll = 0 * RESIZE_COEFFICIENT

#Setup a 300x300 Pixel Display
DISPLAYSERF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
DISPLAYSERF.fill(WHITE)
pygame.display.set_caption("Racing Game")

# Music
mixer = pygame.mixer

mixer.init()
mixer.music.load("gameMusic.ogg")
mixer.music.set_volume(0.7)
mixer.music.play(-1)

#statemachine
states = {
    "Start": States.StartState.StartState(),
    "Play": States.PlayState.PlayState(),
    "Score": States.ScoreState.ScoreState()
}
gStateMachine = StateMachine.StateMachine(states)
gStateMachine.change("Start", None)


def collidCheck(entity1, entity2):
    x1 = entity1.x * RESIZE_COEFFICIENT
    y1 = entity1.y * RESIZE_COEFFICIENT
    x2 = entity2.x * RESIZE_COEFFICIENT
    y2 = entity2.y * RESIZE_COEFFICIENT
    if not (x1 >
            x2 + entity2.width) and not (x1 + entity1.width < x2) and not (
                y1 > y2 + entity2.height) and not (y1 + entity1.height < y2):
        return True
    else:
        return False


def update():
    global groundScroll
    global backgroundScroll
    gStateMachine.update()
    groundScroll = (groundScroll - GROUND_SCROLL_SPEED) % LOOPING_POINT
    Road.rect.topleft = (groundScroll - WINDOW_WIDTH,
                         WINDOW_HEIGHT - Road.rect.height)

    backgroundScroll = (backgroundScroll -
                        BACKGROUND_SCROLL_SPEED) % LOOPING_POINT
    Background.rect.topleft = (backgroundScroll - WINDOW_WIDTH, 0)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def render():
    pygame.display.update()
    DISPLAYSERF.fill(WHITE)

    DISPLAYSERF.blit(Road.image, Road.rect)
    DISPLAYSERF.blit(Background.image, Background.rect)

    gStateMachine.render()


#game loop
while True:
    update()
    render()

    clock.tick(FPS)
