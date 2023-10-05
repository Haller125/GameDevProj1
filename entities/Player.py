from entities.BaseEntity import BaseEntity


class Player(BaseEntity):
    def __init__(self, x, y, health=100, speed=5):
        super().__init__(x, y, health, speed)

    # -1 <= dx <= 1 and -1 <= dy <= 1
    def move(self, dx, dy):
        dx = max(min(dx, 1), -1)
        dy = max(min(dy, 1), -1)
        self.x += self.speed * dx
        self.y += self.speed * dy

    def attack(self, target):
        # Logic for attacking a target
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        # Logic for player death
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
