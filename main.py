# Setup Project

import pygame
import sys

print("Starting Game")

from scripts.const import WIDTH, HEIGHT, BG_COLOR, BLUE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Basic Screen")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)

        self.display = self.screen.copy()

        self.clock = pygame.time.Clock()

        self.rect = pygame.surface.Surface((100, 100))
        self.rect.fill(BLUE)

    def run(self):
        running = True
        while running:
            # For Background ------------------------------------------------------|
            self.display.fill(BG_COLOR)

            self.display.blit(self.rect, (100, 100))
            # Checking Events -----------------------------------------------------|
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    pass
                if event.type == pygame.KEYUP:
                    pass
            # Rendering Screen ----------------------------------------------------|
            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
            )
            pygame.display.update()
            self.clock.tick(60)

    def quit(self):
        # Quit --------------------------------------------------------------------|
        pygame.quit()
        sys.exit()
        exit()


if __name__ == "__main__":
    Game().run()
print("Game Over")
