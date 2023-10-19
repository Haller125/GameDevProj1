from entities.BaseEntity import BaseEntity
import pygame
import modules.Button as Button
import colors as colors
from scenes.MainMenu import MainMenu


class Player(BaseEntity):
    def __init__(self, x, y, health=100, speed=5):
        super().__init__(x, y, health, speed)
        self.startFrame = 0
        self.framerate = 1200
        self.change_color_start_time = pygame.time.get_ticks()

    # -1 <= dx <= 1 and -1 <= dy <= 1
    def move(self, dx, dy):
        dx = max(min(dx, 1), -1)
        dy = max(min(dy, 1), -1)
        self.x += self.speed * dx
        self.y += self.speed * dy

    def border_death(self, max_x, max_y, min_x, min_y):
        if self.x >= max_x - 32 or self.y >= max_y - 32 or self.x <= min_x or self.y <= min_y:
            return True

    def attack(self, target):
        # Logic for attacking a target
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        # Logic for player death
        return "DEATH"

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def draw_death(self, screen):
        self.runTime = True
        while self.runTime:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runTime = False
            red_value = int(
                (self.startFrame / self.framerate) * 255)  # Create the color with the changing red component
            color = (255, 255 - red_value, 255 - red_value)  # Clear the screen
            screen.fill((0, 0, 0))  # Draw the square with the changing color
            pygame.draw.rect(screen, color, (self.x, self.y, 32, 32))
            pygame.display.flip()  # Increment the frame counter
            self.startFrame += 1
            # End the animation after reaching the desired number of frames     
            if self.startFrame >= self.framerate:
                self.runTime = False
