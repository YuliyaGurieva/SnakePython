import pygame
pygame.init()
space_color = (0, 50, 0)
header_color = (0, 100, 50)
snake_color = (0, 100, 0)
size_block = 20
count_blocks = 19
header_field = 70
size = (size_block * count_blocks + size_block * 2, (size_block * count_blocks + size_block * 2) + header_field)
white = (255, 255, 255)
wheat = (245, 222, 179)
black = (0, 0, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake Python')
print(size)
class SnakeWay:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [size_block + column * size_block,
                                     header_field + size_block + row * size_block, size_block, size_block])
snake_way = [SnakeWay(9, 9)]
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
    screen.fill(space_color)
    pygame.draw.rect(screen, header_color, (0, 0, size[0], header_field))
    for row in range(count_blocks):
        for column in range(count_blocks):
            if (row + column) % 2 == 0:
                color = wheat
            else:
                color = black
            draw_block(color, row, column)
    for block in snake_way:
        draw_block(snake_color, block.x, block.y)
    pygame.display.flip()

