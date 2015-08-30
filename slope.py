# slope class
# slope represented by grid of numbers
import random

class Slope:
    def __init__(self, grid_size, max_resistance):
        self.grid_size = grid_size
        self.max_resistance= max_resistance
        self.grid = self.make_grid()
        # self.grid = [[max_resistance]*grid_size] * grid_size
        # You have to create the grid "manually" because if you do it with
        # list comprehensions or multiplication, you aren't creating individual
        # items, you are creating references to the same item, so when you try
        # to update one item, it changes the whole column instead.

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

    def rain_drop(self):
        altitude = 0
        side_to_side = self.pick_start()
        while altitude < self.grid_size:
            self.update_slope(altitude, side_to_side)
            (altitude, side_to_side) = self.pick_next(altitude, side_to_side)
        # update the "hidden" altitude
        self.update_slope(altitude, side_to_side)

    # update the slope when a drop passes the tile
    def update_slope(self, altitude, side_to_side):
        try:
            self.grid[altitude][side_to_side] += 1
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
        west = (altitude, side_to_side - 1, )
        south_west = (altitude + 1, side_to_side - 1)
        south = (altitude + 1, side_to_side)
        south_east = (altitude + 1, side_to_side + 1)
        east = (altitude, side_to_side + 1)

        neighbor_coords = [neighbor for neighbor in \
                [west, south_west, south, south_east, east] \
                if self.in_range(neighbor[0], neighbor[1])]

        neighbors = {}
        for thing in neighbor_coords:
            neighbors[thing] = self.grid[thing[0]][thing[1]]

        return neighbors


    def in_range(self, altitude, side_to_side):
        #return x >= 0 and y >= 0 and x < self.grid_size and y < self.grid_size
        return altitude >= 0 and side_to_side >= 0 and side_to_side < self.grid_size

    def pick_start(self):
        # in Python, randint includes endpoints
        return random.randint(0, self.grid_size-1)

