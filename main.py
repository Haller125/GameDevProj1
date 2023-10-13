import pygame
import colors as colors
from scenes.MainMenu import MainMenu
from scenes.GamePlay import GamePlay
from scenes.DeathScreen import DeathScreen
class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game Title") # future title
        self.scene = MainMenu(self)
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            result = self.scene.process_events()
            if result == "QUIT":
                self.running = False
            elif result == "GAMEPLAY":
                print("Switching to gameplay scene")
                self.scene = GamePlay(self)
            
            elif self.scene.update(self.screen)== "DEATH":       
                print("Switching to death screen")             
                self.scene = DeathScreen(self)
            self.clock.tick(60)
            self.scene.update(self.screen)
            self.scene.render(self.screen)
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()