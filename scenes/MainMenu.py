import pygame
import modules.Button as Button
import colors as colors

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.StartButton = Button.Button(self.game.width/2 - 100, self.game.height/2 - 38,
                                         200, 76, colors.GREEN, "Start", (0, 0, 0))
        self.QuitButton = Button.Button(self.game.width/2 - 75, self.game.height/2 + 50,
                                        150, 50, colors.RED, "Quit", (0, 0, 0))

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

    def update(self):
        if self.StartButton.hover(pygame.mouse.get_pos()):
            self.StartButton.color = colors.BRIGHT_GREEN
        elif self.QuitButton.hover(pygame.mouse.get_pos()):
            self.QuitButton.color = colors.BRIGHT_RED
        else:
            self.StartButton.color = colors.GREEN
            self.QuitButton.color = colors.RED

    def render(self, screen):
        screen.fill((255, 255, 255))
        self.StartButton.draw(screen)
        self.QuitButton.draw(screen)