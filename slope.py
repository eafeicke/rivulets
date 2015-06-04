# slope class
# slope represented by grid of numbers

class Slope:
    def __init__(self, size, max_resistance):
        self.size = size
        self.max_resistance= max_resistance
        self.grid = [[max_resistance]*size] * size

    def rain_drops(self, num_drops): # takes number of drips to drop

if __name__ == "__main__":
    test_slope = Slope(5, 10)
    assert test_slope.size == 5
    assert test_slope.max_resistance == 10
    assert test_slope.grid == [[10,10,10,10,10], \
                               [10,10,10,10,10], \
                               [10,10,10,10,10], \
                               [10,10,10,10,10], \
                               [10,10,10,10,10]]
    print "tests passed"