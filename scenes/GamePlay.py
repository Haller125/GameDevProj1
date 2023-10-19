import pygame
from entities.Player import Player
import colors as colors


class GamePlay:
    def __init__(self, game):
        self.game = game
        self.Player = Player(x=400, y=300)
        self.min_x = 0
        self.min_y = 0
        self.max_x = 800
        self.max_y = 600
        self.is_Player_dead = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif self.is_Player_dead:
                return "DEATH"
        return None

    def update(self, screen):
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

        if self.Player.border_death(self.max_x, self.max_y, self.min_x, self.min_y):
            self.Player.draw_death(screen)
            self.is_Player_dead = True
            return

        self.Player.move(x, y)

    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, colors.GREY, (0, 0, 800, 600), 10)
        self.Player.draw(screen)
