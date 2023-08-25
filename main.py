# Setup Project

import pygame
from random import randint, random
from scripts.utils import DemoObject
import sys

print("Starting Game")

from scripts.const import WIDTH, HEIGHT, BG_COLOR, BLUE, RED


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Basic Screen")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)

        self.display = self.screen.copy()

        self.clock = pygame.time.Clock()

        self.objs = []

        # --------------------------------------------------------------------------
        for i in range(10):
            myPos = (randint(0, WIDTH), randint(0, HEIGHT))
            mySize = (randint(10, 50), randint(10, 50))
            self.objs.append(DemoObject(myPos, mySize))
        # --------------------------------------------------------------------------

    def resize(self):
        prevSize = self.display.get_size()
        currentSize = self.screen.get_size()

        if prevSize != currentSize:
            ratio = (currentSize[0] / prevSize[0], currentSize[1] / prevSize[1])
            print(ratio)
            self.display = pygame.transform.scale(self.display, self.screen.get_size())
            return ratio
        return False

    def run(self):
        running = True
        while running:
            myRatio = self.resize()

            # For Background ------------------------------------------------------|

            self.display.fill(BG_COLOR)
            # For Objs ------------------------------------------------------------|
            if myRatio:
                for obj in self.objs:
                    obj.transformBy(myRatio)

            for obj in self.objs:
                obj.render(self.display)
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
            self.screen.blit(self.display, (0, 0))
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
