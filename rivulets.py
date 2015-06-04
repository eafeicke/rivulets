import pygame
import time

screen_size = 500
resolution = 10

tile_size = screen_size / resolution

screen = pygame.display.set_mode((screen_size, screen_size))

#background = pygame.Surface(screen.get_size())
#background.fill((255, 255, 255))
#background = background.convert()

#screen.blit(background, (0, 0))

for x in range(0, resolution):
    for y in range(0, resolution):
        pix_x = (screen_size / resolution) * x
        pix_y = (screen_size / resolution) * y
        pygame.draw.rect(screen, (0,(pix_x%255), (pix_y%255)), \
                         pygame.Rect(pix_x, pix_y,tile_size, tile_size))

pygame.display.flip()
for i in range(resolution):
    pygame.draw.rect(screen, (255,0,0), \
                     pygame.Rect(i * tile_size, i * tile_size, tile_size, tile_size))
    pygame.display.flip()
    time.sleep(0.5)

    #pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
