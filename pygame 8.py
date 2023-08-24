import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800  # Increased width
screen_height = 600  # Increased height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle dimensions
paddle_width = 15
paddle_height = 100

# Ball dimensions
ball_size = 20

# Paddle speeds
paddle_speed = 6  # Slightly faster paddle

# Initial positions
player_paddle = pygame.Rect(50, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2, ball_size, ball_size)

ball_speed_x = 7
ball_speed_y = 7

# Additional features
opponent_speed = paddle_speed * 1.2  # Faster opponent AI
ball_fast_speed = 10

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_s] and player_paddle.bottom < screen_height:
        player_paddle.y += paddle_speed

    # Improved opponent AI
    if opponent_paddle.centery < ball.centery:
        opponent_paddle.y += opponent_speed
    elif opponent_paddle.centery > ball.centery:
        opponent_paddle.y -= opponent_speed

    # Ball movement with speed adjustment
    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
        ball_speed_x = ball_fast_speed
        ball_speed_y = ball_fast_speed
    else:
        ball_speed_x = 7
        ball_speed_y = 7

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x = -ball_speed_x

    # Clear the screen
    screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, player_paddle)
    pygame.draw.rect(screen, white, opponent_paddle)
    pygame.draw.ellipse(screen, white, ball)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(60)
