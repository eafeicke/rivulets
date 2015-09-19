import pygame
import time

class Board():
    def __init__(self, grid):
        self.grid = grid
        self.screen_size = 100
        self.resolution = len(self.grid[0])
        self.tile_size = self.screen_size / self.resolution
        self.begin_color = (180,130,70)
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.update_entire_board()

    # update the screen based on the grid
    def update_entire_board(self):
        for row in range(self.resolution):
            for col in range(self.resolution):
                self.update_tile(row, col)

    # make update on one tile
    def update_tile(self, row, col):
        tile_val = self.grid[row][col]

        r = self.begin_color[0] - tile_val
        if r < 0:
            r = 0
        g = self.begin_color[1] - tile_val
        if g < 0:
            g = 0
        b = self.begin_color[2] - tile_val
        if b < 0:
            b = 0

        pygame.display.update(pygame.Rect(25, 25, 25, 25))

        new_color = (r, g, b)

        new_rect = pygame.Rect(row * self.tile_size, col * self.tile_size, \
                               self.tile_size, self.tile_size)
        pygame.draw.rect(self.screen, new_color, new_rect)
        pygame.display.update([new_rect])


if __name__ == "__main__":
    test_grid = [
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1]
                ]

    test_board = Board(test_grid)

    time.sleep(3)

    test_board.grid = [
                        [1, 50, 1, 50],
                        [50, 1, 50, 1],
                        [1, 50, 1, 50],
                        [50, 1, 50, 1]
                        ]
    test_board.update_entire_board()

    running = True

    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False