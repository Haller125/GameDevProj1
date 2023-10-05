import pygame
from colors import WHITE

class BaseEntity:
    def __init__(self, x=0, y=0, health=100, speed=5, image=pygame.Surface((32, 32))):
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed
        image.fill(WHITE)
        self.image = image

    def move(self, dx, dy):
        raise NotImplementedError

    def attack(self, target):
        raise NotImplementedError

    def take_damage(self, damage):
        raise NotImplementedError

    def die(self):
        raise NotImplementedError
