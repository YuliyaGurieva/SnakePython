import pygame
import sys
import random

pygame.init()
space_color = (0, 50, 0)
header_color = (0, 100, 50)
snake_color = (0, 100, 0)
size_block = 20
count_blocks = 19
header_field = 70
size = (size_block * count_blocks + size_block * 2, (size_block * count_blocks + size_block * 2) + header_field)
wheat = (245, 222, 179)
black = (0, 0, 0)
yellow = (255, 255, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake Python')
timer = pygame.time.Clock()

class SnakeWay:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_inside(self):
        return 0 <= self.x < count_blocks and 0 <= self.y < count_blocks
    def __eq__(self, other):
        return isinstance(other, SnakeWay) and self.x == other.x and self.y == other.y
def new_food_coords():
    x = random.randint(0, count_blocks - 1)
    y = random.randint(0, count_blocks - 1)
    new_food = SnakeWay(x, y)
    while new_food in snake_ways:
        new_food.x = random.randint(0, count_blocks - 1)
        new_food.y = random.randint(0, count_blocks - 1)
    return new_food
def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [size_block + column * size_block,
                                     header_field + size_block + row * size_block, size_block, size_block])
snake_ways = [SnakeWay(9, 8), SnakeWay(9, 9), SnakeWay(9, 10)]
food = new_food_coords()
dif_row = 0
dif_col = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dif_col != 0:
                dif_row = -1
                dif_col = 0
            elif event.key == pygame.K_DOWN and dif_col != 0:
                dif_row = 1
                dif_col = 0
            elif event.key == pygame.K_LEFT and dif_row != 0:
                dif_row = 0
                dif_col = -1
            if event.key == pygame.K_RIGHT and dif_row != 0:
                dif_row = 0
                dif_col = 1
    screen.fill(space_color)
    pygame.draw.rect(screen, header_color, (0, 0, size[0], header_field))
    for row in range(count_blocks):
        for column in range(count_blocks):
            if (row + column) % 2 == 0:
                color = wheat
            else:
                color = black
            draw_block(color, row, column)
    head = snake_ways[-1]
    if not head.is_inside():
        print('GAME OVER!', 'You are failed!', sep='\n')
        pygame.quit()
        sys.exit()
    draw_block(yellow, food.x, food.y)
    for block in snake_ways:
        draw_block(snake_color, block.x, block.y)

    if food == head:
        food = new_food_coords()

    new_head = SnakeWay(head.x + dif_row, head.y + dif_col)
    snake_ways.append(new_head)
    snake_ways.pop(0)

    pygame.display.flip()
    timer.tick(3)

