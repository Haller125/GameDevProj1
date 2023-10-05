import pygame
from entities.Player import Player

class GamePlay:
    def __init__(self, game):
        self.game = game
        self.Player = Player(x=400, y=300)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            # elif event.type == pygame.KEYDOWN:  # Check for key presses
                # if event.key == pygame.K_LEFT:
                #     self.Player.move(-1, 0)
                # if event.key == pygame.K_RIGHT:
                #     self.Player.move(1, 0)
                # if event.key == pygame.K_UP:
                #     self.Player.move(0, -1)
                # if event.key == pygame.K_DOWN:
                #     self.Player.move(0, 1)
        return None

    def update(self):
        keys = pygame.key.get_pressed()
        x, y = 0, 0
        if keys[pygame.K_LEFT]:
            x += -1
        if keys[pygame.K_RIGHT]:
            x += 1
        if keys[pygame.K_UP]:
            y += -1
        if keys[pygame.K_DOWN]:
            y += 1
        self.Player.move(x, y)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.Player.draw(screen)
