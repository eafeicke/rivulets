# slope class
# slope represented by grid of numbers
import random
import pygame
import time

class Slope:
    def __init__(self, \
                 grid_size=5, \
                 max_resistance=50, \
                 rain_delta=1, \
                 screen_size=100, \
                 mod_west=0, \
                 mod_southwest=0, \
                 mod_south=0, \
                 mod_southeast=0, \
                 mod_east=0, \
                 begin_color=(180,130,70)):

        self.grid_size = grid_size
        self.max_resistance= max_resistance
        self.grid = self.make_grid()
        self.rain_delta = rain_delta
        # self.grid = [[max_resistance]*grid_size] * grid_size
        # You have to create the grid "manually" because if you do it with
        # list comprehensions or multiplication, you aren't creating individual
        # items, you are creating references to the same item, so when you try
        # to update one item, it changes the whole column instead.

        # board stuff
        self.screen_size = screen_size
        self.begin_color = begin_color

        self.resolution = len(self.grid[0])
        self.tile_size = self.screen_size / self.resolution
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))

        self.update_entire_board()

        # Modifiers for picking next direction - we want the drop to
        # be going mostly down
        self.mod_west = mod_west
        self.mod_southwest = mod_southwest
        self.mod_south = mod_south
        self.mod_southeast = mod_southeast
        self.mod_east = mod_east

    def make_grid(self):
        grid = []
        for _ in range(self.grid_size):
            line = []
            for _ in range(self.grid_size):
                line.append(self.max_resistance)
            grid.append(line)
        # "hidden" altitude - terminate here
        hidden_alt = []
        for _ in range(self.grid_size):
            hidden_alt.append(self.max_resistance)
        grid.append(hidden_alt)

        return grid

    def __repr__(self):
        res = ""
        for line in self.grid:
            res += str(line)
            res += "\n"
        return res

    def rain_drop(self, delay_eqn, offset):
        altitude = 0
        side_to_side = self.pick_start()
        drop = 1
        while altitude < self.grid_size:
            self.update_slope(altitude, side_to_side)
            self.update_tile(altitude, side_to_side)
            (altitude, side_to_side) = self.pick_next(altitude, side_to_side)
            pygame.event.pump()
            delay_time = delay_eqn(drop, offset)
            time.sleep(delay_time)
            drop += 1
        # update the "hidden" altitude
        self.update_slope(altitude, side_to_side)
        self.update_tile(altitude, side_to_side)

    # update the slope when a drop passes the tile
    def update_slope(self, altitude, side_to_side):
        try:
            self.grid[altitude][side_to_side] += self.rain_delta
        except IndexError:
            print altitude, side_to_side

    # pick the next tile the drop will go to
    def pick_next(self, altitude, side_to_side):
        neighbors = self.get_neighbors(altitude, side_to_side)
        selection_array = self.create_selection(neighbors)
        return random.choice(selection_array)

    # create an array of coordinates to choose from based on the weight of the
    # tile - example if you choose (0, 0):
    # 0 1
    # 2 3
    # [(0, 1), (0, 1), (1, 1), (1, 1), (1, 1), (1, 0)]
    def create_selection(self, neighbors):
        selection_array = []
        for coord in neighbors.keys():
            for _ in range(neighbors[coord]):
                selection_array.append(coord)
        return selection_array

    # get all of the potential next tiles
    def get_neighbors(self, altitude, side_to_side):
        neighbors = {}
        # west
        w_alt = altitude
        w_sts = side_to_side - 1
        if self.in_range(w_alt, w_sts):
            neighbors[(w_alt, w_sts)] = \
            self.grid[w_alt][w_sts] + self.mod_west

        # southwest
        sw_alt = altitude + 1
        sw_sts = side_to_side - 1
        if self.in_range(sw_alt, sw_sts):
            neighbors[(sw_alt, sw_sts)] = \
            self.grid[sw_alt][sw_sts] + self.mod_southwest

        # south
        s_alt = altitude + 1
        s_sts = side_to_side
        if self.in_range(s_alt, s_sts):
            neighbors[(s_alt, s_sts)] = \
            self.grid[s_alt][s_sts] + self.mod_south

        # southeast
        se_alt = altitude + 1
        se_sts = side_to_side + 1
        if self.in_range(se_alt, se_sts):
            neighbors[(se_alt, se_sts)] = \
            self.grid[se_alt][se_sts] + self.mod_southeast

        # east
        e_alt = altitude
        e_sts = side_to_side + 1
        if self.in_range(e_alt, e_sts):
            neighbors[(e_alt, e_sts)] = \
            self.grid[e_alt][e_sts] + self.mod_east

        return neighbors


    def in_range(self, altitude, side_to_side):
        #return x >= 0 and y >= 0 and x < self.grid_size and y < self.grid_size
        return altitude >= 0 and side_to_side >= 0 and side_to_side < self.grid_size

    def pick_start(self):
        # in Python, randint includes endpoints
        return random.randint(0, self.grid_size-1)

    ###############
    # Board stuff #
    ###############
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

        new_color = (r, g, b)

        new_rect = pygame.Rect(col * self.tile_size, row * self.tile_size, \
                               self.tile_size, self.tile_size)
        pygame.draw.rect(self.screen, new_color, new_rect)
        pygame.display.update([new_rect])

