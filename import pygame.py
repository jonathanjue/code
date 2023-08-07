import pygame
from pygame.locals import *
import random

pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Block Game")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Paddle dimensions
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

# Ball dimensions
BALL_RADIUS = 10

# Block dimensions
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 30

# Paddle properties
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 10
paddle_speed = 5
paddle_length = PADDLE_WIDTH

# Ball properties
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 3
ball_dy = -3

# Power-up properties
powerup_x = 0
powerup_y = 0
powerup_width = 20
powerup_height = 20
powerup_active = False

# Block properties
block_rows = 5
block_cols = 10
block_margin = 5
blocks = []

for row in range(block_rows):
    for col in range(block_cols):
        x = col * (BLOCK_WIDTH + block_margin) + block_margin
        y = row * (BLOCK_HEIGHT + block_margin) + block_margin
        blocks.append(pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT))

def draw_paddle():
    pygame.draw.rect(window, BLUE, (paddle_x, paddle_y, paddle_length, PADDLE_HEIGHT))

def draw_ball():
    pygame.draw.circle(window, RED, (ball_x, ball_y), BALL_RADIUS)

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(window, GREEN, block)

def draw_powerup():
    pygame.draw.rect(window, YELLOW, (powerup_x, powerup_y, powerup_width, powerup_height))

def handle_collision():
    global ball_dx, ball_dy, paddle_length, powerup_active

    if ball_y + BALL_RADIUS >= paddle_y and ball_y + BALL_RADIUS <= paddle_y + PADDLE_HEIGHT and ball_dy > 0:
        if ball_x + BALL_RADIUS >= paddle_x and ball_x - BALL_RADIUS <= paddle_x + paddle_length:
            ball_dy = -ball_dy

    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
            blocks.remove(block)
            ball_dy = -ball_dy
            break

    if powerup_active:
        paddle_length = PADDLE_WIDTH + 50

def generate_powerup():
    global powerup_x, powerup_y, powerup_active
    powerup_x = random.randint(0, WIDTH - powerup_width)
    powerup_y = random.randint(0, HEIGHT // 2)
    powerup_active = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]

    if keys[K_LEFT]:
        paddle_x -= paddle_speed
    if keys[K_RIGHT]:
        paddle_x += paddle_speed

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy
    if ball_y >= HEIGHT:
        # Game over when ball goes below the screen
        running = False

    handle_collision()

    # Power-up logic
    if powerup_active:
        if pygame.Rect(paddle_x, paddle_y, paddle_length, PADDLE_HEIGHT).colliderect(pygame.Rect(powerup_x, powerup_y, powerup_width, powerup_height)):
            powerup_active = False
            paddle_length += 50

    window.fill(BLACK)
    draw_paddle()
    draw_ball()
    draw_blocks()

    if not powerup_active:
        # Generate a power-up if none is currently active
        generate_powerup()
    else:
        draw_powerup()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
