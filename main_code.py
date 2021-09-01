import pygame
pygame.init()
space_color = (0, 100, 0)
size = (400, 600)
size_block = 20
count_blocks = 20
white = (255, 255, 255)
wheat = (245, 222, 179)
black = (0, 0, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake Python')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
    screen.fill(space_color)

    for row in range(count_blocks):
        for column in range(count_blocks):
            if (row + column) % 2 == 0:
                color = wheat
            else:
                color = black
            pygame.draw.rect(screen, color, [10 + column * size_block,
                                             20 + row * size_block, size_block, size_block])
    pygame.display.flip()

