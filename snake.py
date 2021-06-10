import pygame
import math
import random

pygame.init()

# Colors
white = (255,) * 3
orange = (255, 165, 0)
black = (0,) * 3
red = (255, 0, 0)

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game - by Atharv")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)


def draw_score(score):
    text = score_font.render(f"Score: {score}", True, orange)
    game_display.blit(text, [0, 0])


def draw_snake(s_size, snake_pixels):
    for p in snake_pixels:
        pygame.draw.rect(game_display, white, [p[0], p[1], s_size, s_size])


def main():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    fx = round(random.randrange(0, width - snake_size) / 10) * 10
    fy = round(random.randrange(0, width - snake_size) / 10) * 10

    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            draw_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_1:
                        main()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [fx, fy, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for p in snake_pixels[:-1]:
            if p == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        draw_score(snake_length - 1)

        pygame.display.update()

        if (x, y) == (fx, fy):
            fx = round(random.randrange(0, width - snake_size) / 10) * 10
            fy = round(random.randrange(0, width - snake_size) / 10) * 10
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()


if __name__ == '__main__':
    main()
