import pygame
import time

class Display():
    def __init__(self, grid):
        self.grid = grid
        self.screen_size = 500
        self.resolution = len(self.grid)
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

#         running = True
#
#         while running:
#             for event in pygame.event.get():
#                 if event == pygame.QUIT:
#                     running = False

    # update the screen based on the grid
    def update_entire_display(self):
        for row in range(self.resolution):
            for col in range(self.resolution):
                self.update_tile(row, col)

    # make update on one tile
    # (faster than updating entire board)
    def update_tile(self, row, col):
        tile_val = self.grid[row][col]
        new_color = (self.begin_color[0] - tile_val, \
                     self.begin_color[1] - tile_val, \
                     self.begin_color[2] - tile_val)
        new_rect = pygame.Rect(row * self.tile_size, col * self.tile_size, \
                               self.tile_size, self.tile_size)
        pygame.draw.rect(self.screen, new_color, new_rect)
        pygame.display.update(new_rect)


if __name__ == "__main__":
    test_grid = [
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1]
                ]

    test_display = Display(test_grid)

    print "here"
    time.sleep(3)

    test_display.grid = [
                        [1, 50, 1, 50],
                        [50, 1, 50, 1],
                        [1, 50, 1, 50],
                        [50, 1, 50, 1]
                        ]
    test_display.update_entire_display()

    running = True

    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False