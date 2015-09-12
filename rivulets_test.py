import pygame
import time

screen_size = 500
resolution = 15
tile_size = screen_size / resolution
screen = pygame.display.set_mode((screen_size, screen_size))

# colors
r = 180
g = 130
b = 70
# 171, 120, 65
# 140, 88, 32
# 122, 74, 22
# 89, 49, 6
# 69, 36, 0

for i in range(10):
    pygame.draw.rect(screen, (r,g,b), pygame.Rect(0, 0, 500, 500))
    r -= 15
    g -= 15
    b -= 15
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    pygame.display.flip()
    time.sleep(0.5)

# for x in range(0, resolution):
#     for y in range(0, resolution):
#         pix_x = (screen_size / resolution) * x
#         pix_y = (screen_size / resolution) * y
#         pygame.draw.rect(screen, (r,g,b), \
#                          pygame.Rect(pix_x, pix_y,tile_size, tile_size))
#
# pygame.board.flip()

# This keeps the window open after the code is done executing
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event == pygame.QUIT:
#             running = False
