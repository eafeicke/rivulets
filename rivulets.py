import pygame
import math
from slope import Slope

grid_size = 50
max_resistance = 1
rain_delta = 15
screen_size = 600
mod_west = 0
mod_southwest = 5
mod_south = 6
mod_southeast = 5
mod_east = 0
offset = 0.15
#begin_color = (110, 60, 0)

def drop_delay_eqn(x, drop_offset):
    # y = (-1/100000) * (x ^ 2) + 0.5
    thing = ((-1.0 / 10000.0) * math.pow(x, 2)) + drop_offset
    return thing if thing > 0.05 else 0.05 

slope = Slope(grid_size, max_resistance, rain_delta, screen_size, mod_west, \
              mod_southwest, mod_south, mod_southeast, mod_east)#, begin_color)

drops = 100
for drop in range(drops):
    # do the thing
    slope.rain_drop(drop_delay_eqn, offset)
    #time.sleep(0.)

print "done"

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
