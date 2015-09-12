import pygame
import time
from slope import Slope

# screen_size = 500
# resolution = 15
# tile_size = screen_size / resolution
# screen = pygame.board.set_mode((screen_size, screen_size))
# begin_color = (180,130,70)
#
# for x in range(0, resolution):
#     for y in range(0, resolution):
#         pix_x = (screen_size / resolution) * x
#         pix_y = (screen_size / resolution) * y
#         pygame.draw.rect(screen, (0,(pix_x%255), (pix_y%255)), \
#                          pygame.Rect(pix_x, pix_y,tile_size, tile_size))
#
# pygame.board.flip()
#
# for i in range(resolution):
#     pygame.draw.rect(screen, (255,0,0), \
#                      pygame.Rect(i * tile_size, i * tile_size, tile_size, tile_size))
#     pygame.board.flip()
#     time.sleep(0.5)
slope = Slope(5, 50)

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
