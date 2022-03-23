import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

width = 600
height = 400

size = (600, 400)

dis = pygame.display.set_mode(size)

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

game_over = False
game_close = False

x1 = width / 2 # Holder styr på første variabel i lista
y1 = height / 2

x1_change = 0
y1_change = 0

snake_list = []
snake_length = 1

foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

while not game_over:
    while game_close is True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_close = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(black)
    pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_close = True

    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        snake_length += 1
        snake_speed += 1
        print("Score: " + str(snake_length))

    clock.tick(snake_speed)

pygame.quit()
