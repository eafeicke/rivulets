import pygame
import time
from slope import Slope

grid_size = 10
screen_size = 500

slope = Slope(grid_size, screen_size)

drops = 100
for drop in range(drops):
    # do the thing
    print drop
    slope.rain_drop()
    time.sleep(0.25)

print "done"

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
