from colors import WHITE

import pygame

class Player:
    def __init__(self, x, y, health=100, speed=5, image=pygame.Surface((32, 32))):
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

    def melee_attack(self, target):
        distance = self.distance_to(target)
        if distance <= self.attack_range:
            print("Attacking")
            target.take_damage(self.melee_damage)  # Adjust the damage value as needed

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
