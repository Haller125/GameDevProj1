import pygame
from entities.Player import Player
from entities.Dummy import Dummy
import colors as colors


class GamePlay:
    def __init__(self, game):
        self.game = game
        self.Player = Player(x=400, y=300)
        self.Dummy = Dummy(x=200, y=200)
        self.min_x = 0
        self.min_y = 0
        self.max_x = game.width
        self.max_y = game.height
        self.is_Player_dead = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif self.is_Player_dead:
                return "DEATH"
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.Player.melee_attack(self.Dummy)
                    return None
        return None

    def update(self, screen):
        if self.Player.border_death(self.max_x, self.max_y, self.min_x, self.min_y):
            self.Player.draw_death(screen)
            self.is_Player_dead = True
            return

        keys = pygame.key.get_pressed()
        x, y = 0, 0
        if keys[pygame.K_a]:
            x += -1
        if keys[pygame.K_d]:
            x += 1
        if keys[pygame.K_w]:
            y += -1
        if keys[pygame.K_s]:
            y += 1
        self.Player.move(x, y)
        self.Player.update()

        if keys[pygame.K_SPACE]:
            self.Player.dash()

    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, colors.GREY, (0, 0, self.game.width, self.game.height), 10)
        self.Player.draw(screen)
        self.Dummy.draw(screen)
