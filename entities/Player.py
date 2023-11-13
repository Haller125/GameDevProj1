from colors import WHITE

import pygame

from entities.Arrow import Arrow
from entities.State import *

class Player:
    def __init__(self, x, y, health=100, speed=5, image=None):
        if image is None:
            image = pygame.Surface((32, 32))
            image.fill(WHITE)
        self.image = image
        self.x, self.y = x, y
        self.health = health
        self.speed = speed
        self.startFrame = 0
        self.framerate = 1200
        self.change_color_start_time = pygame.time.get_ticks()
        self.width, self.height = 32, 32
        self.attack_range = 50
        self.melee_damage = 10
        self.state = IDLE
        # Melee attack
        self.melee_attack_start = 0
        self.melee_attack_lock_time = 150
        self.melee_attack_cooldown = 500
        # Dash
        self.dash_start = 0
        self.dash_lock_time = 100
        self.dash_cooldown = 500
        self.last_dx = 0
        self.last_dy = 0
        # Range attack
        self.arrows = []
        self.range_attack_start = 0
        self.range_attack_cooldown = 500

    # -1 <= dx <= 1 and -1 <= dy <= 1
    def move(self, dx, dy, speed=None):
        delta = speed if speed is not None else self.speed
        if self.state not in (DASHING, DYING, ATTACKING):
            self.change_position(dx, dy, delta)

    def change_position(self, dx, dy, delta):
        self.last_dx, self.last_dy = dx, dy
        dx = max(min(dx, 1), -1)
        dy = max(min(dy, 1), -1)
        self.x += delta * dx
        self.y += delta * dy

    def melee_attack(self, target):
        current_time = pygame.time.get_ticks()
        if (self.state == IDLE or self.state == MOVING) and (current_time - self.melee_attack_start >= self.melee_attack_cooldown):
            self.state = ATTACKING
            self.melee_attack_start = pygame.time.get_ticks()
            distance = self.distance_to(target)
            if distance <= self.attack_range:
                print("Attacking")
                   # Adjust the damage value as needed

    def ranged_attack(self, target):
        current_time = pygame.time.get_ticks()
        if current_time - self.range_attack_start >= self.range_attack_cooldown:
            self.arrows.append(Arrow(self.x, self.y, target))

    def dash(self):
        current_time = pygame.time.get_ticks()
        if (self.state == IDLE or self.state == MOVING) and (current_time - self.dash_start >= self.dash_cooldown):
            self.state = DASHING
            self.dash_start = pygame.time.get_ticks()

    def border_death(self, max_x, max_y, min_x, min_y):
        if self.x >= max_x - 32 or self.y >= max_y - 32 or self.x <= min_x or self.y <= min_y:
            return True

    def distance_to(self, target):
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        # Logic for player death
        return "DEATH"

    def draw(self, screen):
        screen.blit(self.image, ( max(min((self.x - (self.width * 0.5 - 1)), screen.get_width()), 0),
                                  max(min((self.y - (self.height * 0.5 - 2)), screen.get_height()), 0 )))
        for arrow in self.arrows:
            arrow.draw(screen)

    def update(self):
        current_time = pygame.time.get_ticks()

        for arrow in self.arrows:
            arrow.update()

        if self.state == DYING:
            # if current_time - self.death_time > self.framerate:
            #     self.die()
            pass

        elif self.state == DASHING:
            print("Dashing")
            self.change_position(self.last_dx, self.last_dy, self.speed * 3)
            print(self.last_dx, self.last_dy, self.speed * 3)
            if current_time - self.dash_start > self.dash_lock_time:  # Duration of the dash
                self.state = IDLE

        elif self.state == ATTACKING:
            # Duration of the attack animation or effect
            if current_time - self.melee_attack_start >= self.melee_attack_lock_time:
                self.state = IDLE

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
