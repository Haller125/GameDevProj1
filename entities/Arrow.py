import pygame
import math

from colors import RED

class Arrow:
    def __init__(self, x, y, target, width=20, height=2, speed=15, image=None):
        if image is None:
            image = pygame.Surface((width, height), pygame.SRCALPHA)
            image.fill(RED)
        self.image = image
        self.x, self.y = x, y
        self.target = target

        self.speed = speed
        self.width, self.height = width, height
        dx, dy = target.x - x, target.y - y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        self.dir_x, self.dir_y = dx / distance, dy / distance

        self.angle = math.degrees(math.atan2(-dy, dx))
        self.image = pygame.transform.rotate(self.image, self.angle)

        self.rect = pygame.Rect(x, y, width, height)
        self.born = pygame.time.get_ticks()

        self.is_hit = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed

        self.rect.x = self.x
        self.rect.y = self.y

        if self.rect.colliderect(self.target.rect) and not self.is_hit:
            self.target.take_damage(10)
            self.is_hit = True

    def is_dead(self):
        return pygame.time.get_ticks() - self.born > 1000
