import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
PADDLE_SPEED = 3
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
enemy_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up ball
BALL_RADIUS = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
ball_speed_x = BALL_SPEED_X * random.choice([-1, 1])  # Random initial direction
ball_speed_y = BALL_SPEED_Y * random.choice([-1, 1])  # Random initial direction

# Set up game clock
clock = pygame.time.Clock()

# Set up score counter
player_score = 0
enemy_score = 0
font = pygame.font.Font(None, 36)

# Initialize game difficulty
easy_mode = False

# Initialize player's paddle size
player_paddle_width = PADDLE_WIDTH
player_paddle_height = PADDLE_HEIGHT

# Initialize paddle size toggle
paddle_toggle = False

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                # Toggle easy mode
                easy_mode = not easy_mode
            elif event.key == K_p:
                # Toggle player's paddle size
                paddle_toggle = not paddle_toggle
                if paddle_toggle:
                    # Increase player's paddle size
                    player_paddle_width += 30
                    player_paddle_height += 120
                else:
                    # Reset player's paddle size
                    player_paddle_width = PADDLE_WIDTH
                    player_paddle_height = PADDLE_HEIGHT

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[K_w] and player_paddle.y > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[K_s] and player_paddle.y < HEIGHT - player_paddle_height:
        player_paddle.y += PADDLE_SPEED

    # AI-controlled enemy paddle
    if easy_mode:
        if ball.y < enemy_paddle.y + enemy_paddle.height // 2 and enemy_paddle.y > 0:
            enemy_paddle.y -= PADDLE_SPEED // 2  # Slower speed in easy mode
        if ball.y > enemy_paddle.y + enemy_paddle.height // 2 and enemy_paddle.y < HEIGHT - enemy_paddle.height:
            enemy_paddle.y += PADDLE_SPEED // 2  # Slower speed in easy mode
    else:
        if ball.y < enemy_paddle.y + enemy_paddle.height // 2 and enemy_paddle.y > 0:
            enemy_paddle.y -= PADDLE_SPEED
        if ball.y > enemy_paddle.y + enemy_paddle.height // 2 and enemy_paddle.y < HEIGHT - enemy_paddle.height:
            enemy_paddle.y += PADDLE_SPEED

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Handle ball collisions
    if ball.y <= 0 or ball.y >= HEIGHT - BALL_RADIUS:
        ball_speed_y *= -1
    if ball.colliderect(player_paddle) or ball.colliderect(enemy_paddle):
        ball_speed_x *= -1

    # Handle ball going off-screen
    if ball.x <= 0:
        enemy_score += 1
        ball_speed_x = BALL_SPEED_X * random.choice([-1, 1])
        ball_speed_y = BALL_SPEED_Y * random.choice([-1, 1])
        ball.x = WIDTH // 2 - BALL_RADIUS // 2
        ball.y = HEIGHT // 2 - BALL_RADIUS // 2
    if ball.x >= WIDTH - BALL_RADIUS:
        player_score += 1
        ball_speed_x = BALL_SPEED_X * random.choice([-1, 1])
        ball_speed_y = BALL_SPEED_Y * random.choice([-1, 1])
        ball.x = WIDTH // 2 - BALL_RADIUS // 2
        ball.y = HEIGHT // 2 - BALL_RADIUS // 2

    # Check win condition
    if player_score >= 10:
        result = "You win!"
        running = False
    elif enemy_score >= 10:
        result = "Enemy wins!"
        running = False

    # Update screen
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, player_paddle)
    pygame.draw.rect(WIN, WHITE, enemy_paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display score
    score_text = font.render(f"Player: {player_score}  Enemy: {enemy_score}", True, WHITE)
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    pygame.display.update()
    clock.tick(60)

# Display the result
result_text = font.render(result, True, WHITE)
WIN.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 2 - result_text.get_height() // 2))
pygame.display.update()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Quit the game
pygame.quit()
