from slope import Slope

if __name__ == "__main__":
    print "slope creation"
    test_slope = Slope(5, 10)
    assert test_slope.grid_size == 5
    assert test_slope.max_resistance == 10
    assert test_slope.grid == [[10,10,10,10,10], \
                               [10,10,10,10,10], \
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
    assert test_slope.in_range(5, 1) == True
    assert test_slope.in_range(5, 5) == False
    print "get_neighbors"
    assert len(test_slope.get_neighbors(0, 0)) == 3
    assert test_slope.get_neighbors(0, 0).values() == [10, 10, 10]

    assert len(test_slope.get_neighbors(1, 1)) == 5
    assert test_slope.get_neighbors(1, 1).values() == [10, 10, 10, 10, 10]

    #assert len(test_slope.get_neighbors(4, 4)) == 1
    #assert test_slope.get_neighbors(4, 4).values() == [10]
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
    # hardiness check
    for _ in range(100):
        test_slope.rain_drop()
    print test_slope

    big_slope = Slope(10,1)
    print big_slope
    for _ in range(100):
        big_slope.rain_drop()
    print big_slope

    test_slope.grid = [[1, 50, 1, 50, 1], \
                       [50, 1, 50, 1, 50], \
                       [1, 50, 1, 50, 1], \
                       [50, 1, 50, 1, 50], \
                       [1, 50, 1, 50, 1], \
                       [1, 1, 1, 1, 1]]
    test_slope.update_entire_board()

    print "---------------------"
    print "tests passed"