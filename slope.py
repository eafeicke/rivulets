# slope class
# slope represented by grid of numbers
import random

class Slope:
    def __init__(self, grid_size, max_resistance):
        self.grid_size = grid_size
        self.max_resistance= max_resistance
        self.grid = [[max_resistance]*grid_size] * grid_size

    def rain_drop(self):
        side_to_side = self.pick_start()
        altitude = 0
        while altitude < self.grid_size - 1:
            self.update_slope(side_to_side, altitude)
            side_to_side = self.pick_next(side_to_side, altitude)

    # update the slope when a drop passes the tile
    def update_slope(self, side_to_side, altitude):
        self.grid[side_to_side][altitude] = self.grid[side_to_side][altitude] + 1

    # pick the next tile the drop will go to
    def pick_next(self, side_to_side, altitude):
        neighbors = self.get_neighbors(side_to_side, altitude)
        selection_array = self.create_selection(neighbors)
        return random.choice(selection_array)

    def create_selection(self, neighbors):
        selection_array = []
        for coord in neighbors.keys():
            for _ in range(neighbors[coord]):
                selection_array.append(coord)


    def get_neighbors(self, side_to_side, altitude):
        west = (side_to_side - 1, altitude)
        south_west = (side_to_side - 1, altitude + 1)
        south = (side_to_side, altitude + 1)
        south_east = (side_to_side + 1, altitude + 1)
        east = (side_to_side + 1, altitude)
        neighbor_coords = [neighbor for neighbor in \
                [west, south_west, south, south_east, south, east] \
                if self.in_range(neighbor[0], neighbor[1])]
        neighbors = {}
        for thing in neighbor_coords:
            neighbors[thing] = self.grid[thing[0]][thing[1]]
        return neighbors


    def in_range(self, x, y):
        return x >= 0 and y >= 0 and x < self.grid_size and y < self.grid_size

    def pick_start(self):
        return random.randint(0, self.grid_size)

if __name__ == "__main__":
    print "slope creation"
    test_slope = Slope(5, 10)
    assert test_slope.grid_size == 5
    assert test_slope.max_resistance == 10
    assert test_slope.grid == [[10,10,10,10,10], \
                               [10,10,10,10,10], \
                               [10,10,10,10,10], \
                               [10,10,10,10,10], \
                               [10,10,10,10,10]]
    print "in_range"
    assert test_slope.in_range(0, 0) == True
    assert test_slope.in_range(4, 0) == True
    assert test_slope.in_range(0, 4) == True
    assert test_slope.in_range(4, 4) == True
    assert test_slope.in_range(2, 2) == True
    assert test_slope.in_range(-1, 0) == False
    assert test_slope.in_range(0, -1) == False
    print "get_neighbors"
    assert len(test_slope.get_neighbors(0, 0)) == 3
    assert test_slope.get_neighbors(0, 0).values() == [10, 10, 10]

    assert len(test_slope.get_neighbors(1, 1)) == 5
    assert test_slope.get_neighbors(1, 1).values() == [10, 10, 10, 10, 10]

    assert len(test_slope.get_neighbors(4, 4)) == 1
    assert test_slope.get_neighbors(4, 4).values() == [10]
    print "pick_next"
    print "update_slope"
    print "rain_drops"
    print "---------------------"
    print "tests passed"