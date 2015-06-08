# slope class
# slope represented by grid of numbers
import random

class Slope:
    def __init__(self, grid_size, max_resistance):
        self.grid_size = grid_size
        self.max_resistance= max_resistance
        self.grid = [[max_resistance]*grid_size] * grid_size

    def __repr__(self):
        res = ""
        for line in self.grid:
            res += str(line)
            res += "\n"
        return res

    def rain_drop(self):
        altitude = 0
        side_to_side = self.pick_start()
        while altitude < self.grid_size - 1:
            self.update_slope(altitude, side_to_side)
            side_to_side = self.pick_next(altitude, side_to_side)

    # update the slope when a drop passes the tile
    def update_slope(self, altitude, side_to_side):
        self.grid[altitude][side_to_side] = self.grid[altitude][side_to_side] + 1

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
    print "create_selection"
    test_slope2 = Slope(6, 10)
    test_slope2.grid = [[1,2,3, 4 ,5, 6], \
                        [7,8,9,101,1000,102], \
                        [11,12,13,14,15,16], \
                        [17,18,19,20,21,22], \
                        [23,24,25,26,27,28], \
                        [29,30,31,32,33,34]]
    print test_slope2.grid[0][1]
    neighbors = test_slope2.get_neighbors(0,1)
    print neighbors
    print test_slope2.create_selection(neighbors)
    print len(test_slope2.create_selection(neighbors))

    print "pick_next"
    next_pick_test = {}
    for _ in range(500):
        next_thing = test_slope2.pick_next(0, 4)
        if next_thing in next_pick_test:
            next_pick_test[next_thing] += 1
        else:
            next_pick_test[next_thing] = 1
    print next_pick_test
    print "update_slope"
    test_slope2.update_slope(0, 0)
    assert test_slope2.grid[0][0] == 2
    print "rain_drop"
    print test_slope
    test_slope.rain_drop()
    print test_slope
    print "---------------------"
    print "tests passed"