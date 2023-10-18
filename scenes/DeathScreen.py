import pygame
import modules.Button as Button
import colors as colors


class DeathScreen:
    def __init__(self, game):
        self.game = game
        self.StartButton = Button.Button(self.game.width / 2 - 100, self.game.height / 2 - 38, 200, 76, colors.GREEN,
                                         "Start", (0, 0, 0))
        self.QuitButton = Button.Button(self.game.width / 2 - 75, self.game.height / 2 + 50, 150, 50, colors.RED,
                                        "Quit", (0, 0, 0))
        self.square_size = 32
        self.skull_color = colors.GREY
        self.starting_x = self.game.width / 2 - 100
        self.starting_y = self.game.height / 2 - 160
        self.draw_x = self.starting_x
        self.draw_y = self.starting_y
        self.last_update_time = 0

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.StartButton.hover(pygame.mouse.get_pos()):
                    return "GAMEPLAY"
                elif self.QuitButton.hover(pygame.mouse.get_pos()):
                    return "QUIT"
        return None

    def update(self, screen):
        if self.StartButton.hover(pygame.mouse.get_pos()):
            self.StartButton.color = colors.BRIGHT_GREEN
        elif self.QuitButton.hover(pygame.mouse.get_pos()):
            self.QuitButton.color = colors.BRIGHT_RED
        else:
            self.StartButton.color = colors.GREEN
            self.QuitButton.color = colors.RED

    def skull(self, screen):
        # skull drawing
        self.starting_x = self.game.width / 2 - 100
        self.starting_y = self.game.height / 2 - 160
        self.draw_x = self.starting_x
        self.draw_y = self.starting_y
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > 5:
            for i in range(7):
                pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                pygame.display.flip()
                pygame.time.delay(5)
                self.draw_x += 32
            self.draw_x = self.starting_x - 32
            self.draw_y += 32
            for i in range(9):
                pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                self.draw_x += 32
                pygame.display.flip()
                pygame.time.delay(5)
            self.draw_y += 32
            self.draw_x = self.starting_x - 32
            for i in range(9):
                pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                self.draw_x += 32
                pygame.display.flip()
                pygame.time.delay(5)
            self.draw_x = self.starting_x - 32 - 32
            self.draw_y += 32
            for i in range(11):
                if i == 3 or i == 4 or i == 6 or i == 7:
                    pass
                else:
                    pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                self.draw_x += 32
                pygame.display.flip()
                pygame.time.delay(5)
            self.draw_x = self.starting_x - 32 - 32
            self.draw_y += 32
            for i in range(11):
                if i == 2 or i == 3 or i == 4 or i == 6 or i == 7 or i == 8:
                    pass
                else:
                    pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                self.draw_x += 32
                pygame.display.flip()
                pygame.time.delay(5)

            self.draw_x = self.starting_x - 32 - 32
            self.draw_y += 32
            for i in range(11):
                if i == 2 or i == 3 or i == 7 or i == 8:
                    pass
                else:
                    pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                self.draw_x += 32
                pygame.display.flip()
                pygame.time.delay(5)

            self.draw_x = self.starting_x - 32
            self.draw_y += 32
            for i in range(9):
                pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                self.draw_x += 32
                pygame.display.flip()
                pygame.time.delay(5)
            self.draw_x = self.starting_x - 32
            self.draw_y += 32
            for i in range(9):
                if i == 4:
                    pass
                else:
                    pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                self.draw_x += 32
                pygame.display.flip()
                pygame.time.delay(5)
            self.draw_x = self.starting_x + 32
            self.draw_y += 32
            for i in range(5):
                pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                self.draw_x += 32
                pygame.display.flip()
                pygame.time.delay(5)
            self.draw_x = self.starting_x + 32
            self.draw_y += 32
            for i in range(5):
                if i == 1 or i == 3:
                    pass
                else:
                    pygame.draw.rect(screen, colors.GREY, (self.draw_x, self.draw_y, self.square_size, self.square_size))
                self.draw_x += 32
                pygame.display.flip()
                pygame.time.delay(5)
            pygame.time.delay(2000)
            self.last_update_time = current_time

    def render(self, screen):
        screen.fill(colors.RED)
        self.skull(screen)
