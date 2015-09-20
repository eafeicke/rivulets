import pygame
from slope import Slope

grid_size = 50
max_resistance = 50
rain_delta = 10
screen_size = 500
mod_west = 0
mod_southwest = 2
mod_south = 4
mod_southeast = 2
mod_east = 0

slope = Slope(grid_size, max_resistance, rain_delta, screen_size, mod_west, mod_southwest, mod_south, mod_southeast, mod_east)

drops = 100
for drop in range(drops):
    # do the thing
    print drop
    slope.rain_drop()
    #time.sleep(0.)

print "done"

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
