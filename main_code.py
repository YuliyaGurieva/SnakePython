import pygame
import sys
import random
import pygame_menu

pygame.init()
bg_image = pygame.image.load('snake.jpg')
space_color = (0, 50, 0)
header_color = (0, 100, 50)
snake_color = (0, 100, 0)
size_block = 20
count_blocks = 19
header_field = 70
size = (size_block * count_blocks + size_block * 2, (size_block * count_blocks + size_block * 2) + header_field)
wheat = (245, 222, 179)
black = (205, 133, 63)
red = (255, 0, 0)
green = (0, 255, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake Python')
timer = pygame.time.Clock()
font_total = pygame.font.SysFont('courier', 20, bold='Hashable')
font_speed = pygame.font.SysFont('courier', 20, bold='Hashable')


class SnakeWay:
    """ The class is using for creating snake's parts and food. It's also responsible for verification of crossings."""

    def __init__(self, x, y):  # Coordinates
        self.x = x
        self.y = y

    def is_inside(self):  # Control of borders
        return 0 <= self.x < count_blocks and 0 <= self.y < count_blocks

    def __eq__(self, other):  # Control of crossing snake's head with food
        return isinstance(other, SnakeWay) and self.x == other.x and self.y == other.y


def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [size_block + column * size_block,
                                     header_field + size_block + row * size_block, size_block, size_block])


def start_the_game():
    def new_food_coords():
        x = random.randint(0, count_blocks - 1)
        y = random.randint(0, count_blocks - 1)
        new_food = SnakeWay(x, y)
        while new_food in snake_ways:
            new_food.x = random.randint(0, count_blocks - 1)
            new_food.y = random.randint(0, count_blocks - 1)
        return new_food

    snake_ways = [SnakeWay(9, 8), SnakeWay(9, 9), SnakeWay(9, 10)]
    food = new_food_coords()
    dif_row = key_row = 0
    dif_col = key_col = 1
    total = 0
    speed = 2

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dif_col != 0:
                    key_row = -1
                    key_col = 0
                elif event.key == pygame.K_DOWN and dif_col != 0:
                    key_row = 1
                    key_col = 0
                elif event.key == pygame.K_LEFT and dif_row != 0:
                    key_row = 0
                    key_col = -1
                if event.key == pygame.K_RIGHT and dif_row != 0:
                    key_row = 0
                    key_col = 1
        screen.fill(space_color)
        pygame.draw.rect(screen, header_color, (0, 0, size[0], header_field))
        text_total = font_total.render(f'Your progress: {total}', False, green)
        text_speed = font_total.render(f'Speed: {speed}', False, green)
        screen.blit(text_total, (size_block, size_block))
        screen.blit(text_speed, (size_block + 250, size_block))
        for row in range(count_blocks):
            for column in range(count_blocks):
                if (row + column) % 2 == 0:
                    color = wheat
                else:
                    color = black
                draw_block(color, row, column)
        head = snake_ways[-1]
        global bg_image
        if not head.is_inside():
            bg_image = pygame.image.load('snake.jpg')
            break
        draw_block(red, food.x, food.y)
        for block in snake_ways:
            draw_block(snake_color, block.x, block.y)
        pygame.display.flip()
        if food == head:
            total += 1
            if total % 5 == 0:
                speed += 1
            snake_ways.append(food)
            food = new_food_coords()
        dif_row = key_row
        dif_col = key_col
        new_head = SnakeWay(head.x + dif_row, head.y + dif_col)

        if new_head in snake_ways:
            bg_image = pygame.image.load('snake.jpg')
            break
        if total == 20:
            bg_image = pygame.image.load('balls.png')
            break
        snake_ways.append(new_head)
        snake_ways.pop(0)

        timer.tick(speed)


main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.6)
menu = pygame_menu.Menu('', 300, 220,
                        theme=main_theme)

menu.add.text_input('Name: ', default='Guest')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:

    screen.blit(bg_image, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()
