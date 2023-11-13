from colors import WHITE, GREY

import pygame

class Dummy:
    def __init__(self, x, y, health=100, speed=5, image=pygame.Surface((32, 32))):
        self.dx = 5
        image.fill(GREY)
        self.image = image
        self.x, self.y = x, y
        self.health = 10000000000
        self.width, self.height = 32, 32
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.image, (max(min((self.x - (self.width * 0.5 - 1)), screen.get_width()), 0),
                                 max(min((self.y - (self.height * 0.5 - 2)), screen.get_height()), 0)))

    def take_damage(self, amount):
        self.health -= amount
        print("Took damage:", amount)
        print("Health:", self.health)

    def update(self):
        if self.x > 800:
            self.dx = -5
        elif self.x < 100:
            self.dx = 5
        self.x += self.dx
