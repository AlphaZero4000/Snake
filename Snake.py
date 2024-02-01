import pygame as pg
import random
pg.init()


SQUARE_SIZE = 25
NUM_SQUARES = 20
BORDER_WIDTH = 1

SCREEN_WIDTH = SQUARE_SIZE * NUM_SQUARES
SCREEN_HEIGHT = SQUARE_SIZE * NUM_SQUARES
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0))
pg.display.set_caption("Snake Game")

GREEN = (0, 255, 0)
RED = (255, 0, 0)

snake = [[5, 5], [5, 6], [5, 7]]
apple = (5, 10)

def inSnake(x, y):
    for pos in snake[:-1]:
        if x == pos[0] and y == pos[1]:
            return True
    return False

direction = ''
lose = False
run = True
moved = True

while run:
    pg.time.delay(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN and moved:
            if event.key == pg.K_DOWN and direction != 'up' and direction != 'down':
                direction = 'down'
            if event.key == pg.K_UP and direction != 'up' and direction != 'down':
                direction = 'up'
            if event.key == pg.K_LEFT and direction != 'left' and direction != 'right':
                direction = 'left'
            if event.key == pg.K_RIGHT and direction != 'left' and direction != 'right':
                direction = 'right'
            moved = False

    if (not lose):        
        screen.fill((0, 0, 0))
        pg.draw.rect(screen, RED, (apple[0] * SQUARE_SIZE + BORDER_WIDTH, apple[1] * SQUARE_SIZE + BORDER_WIDTH, SQUARE_SIZE - 2 * BORDER_WIDTH, SQUARE_SIZE - 2 * BORDER_WIDTH))
        
        if direction == 'right':      
            snake.append([snake[len(snake) - 1][0] + 1, snake[len(snake) - 1][1]])       
        if direction == 'left':
            snake.append([snake[len(snake) - 1][0] - 1, snake[len(snake) - 1][1]])
        if direction == 'up':
            snake.append([snake[len(snake) - 1][0], snake[len(snake) - 1][1] - 1])
        if direction == 'down':
            snake.append([snake[len(snake) - 1][0], snake[len(snake) - 1][1] + 1])
        moved = True
        if inSnake(snake[len(snake) - 1][0], snake[len(snake) - 1][1]) or snake[len(snake) - 1][0] < 0 or snake[len(snake) - 1][0] >= NUM_SQUARES or snake[len(snake) - 1][1] < 0 or snake[len(snake) - 1][1] >= NUM_SQUARES:
            font = pg.font.SysFont(None, 20)
            img = font.render("You lose", True, (255, 255, 255))
            screen.blit(img, (100, 120))
            lose = True
        if snake[len(snake) - 1][0] != apple[0] or snake[len(snake) - 1][1] != apple[1]:
            if direction != '':
                snake.pop(0)
        else:
            while (True):
                apple = (random.randint(0, NUM_SQUARES - 1), random.randint(0, NUM_SQUARES - 1))
                if not inSnake(apple[0], apple[1]):
                    pg.time.delay(100)
                    break
        
        for pos in snake:
            pg.draw.rect(screen, GREEN, (pos[0] * SQUARE_SIZE + BORDER_WIDTH, pos[1] * SQUARE_SIZE + BORDER_WIDTH, SQUARE_SIZE - 2 * BORDER_WIDTH, SQUARE_SIZE - 2 * BORDER_WIDTH))
        font = pg.font.SysFont(None, 20)
        img = font.render("Score: " + str(len(snake)), True, (255, 255, 255))
        screen.blit(img, (70, 120))
        pg.display.update()
pg.quit()


