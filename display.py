import pygame
import time
from _sqlite3 import Row

class Display():
    def __init__(self, grid):
        self.grid = grid
        self.screen_size = 500
        self.resolution = 15
        self.tile_size = self.screen_size / self.resolution
        self.begin_color = (180,130,70)
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))

        # initialize the screen
        for x in range(0, self.resolution):
            for y in range(0, self.resolution):
                pix_x = (self.screen_size / self.resolution) * x
                pix_y = (self.screen_size / self.resolution) * y
                pygame.draw.rect(self.screen, (self.begin_color), \
                                 pygame.Rect(pix_x, pix_y, self.tile_size, self.tile_size))

        pygame.display.flip()

        running = True

        while running:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    running = False

    # update the screen based on the grid
    def update_entire_display(self):
        for row in range(self.resolution):
            for col in range(self.resolution):
                pass

        for i in range(self.resolution):
            pygame.draw.rect(self.screen, (255,0,0), \
                             pygame.Rect(i * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size))
        pygame.display.flip()
        time.sleep(0.5)

    # make update on one tile
    # (faster than updating entire board)
    def update_tile(self):
        pass


if __name__ == "__main__":
    test_grid = [
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1]
                ]

    test_display = Display(test_grid)
    test_display.start_display()