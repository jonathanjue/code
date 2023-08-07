import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Retro Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 5

# Set up the obstacle
obstacle_size = 50
obstacle_x = random.randint(0, width - obstacle_size)
obstacle_y = -obstacle_size
obstacle_speed = 3

# Set up the clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Update the obstacle position
    obstacle_y += obstacle_speed

    # Check for collision
    if player_x < obstacle_x + obstacle_size and player_x + player_size > obstacle_x \
            and player_y < obstacle_y + obstacle_size and player_y + player_size > obstacle_y:
        running = False

    # Draw the game objects
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(window, WHITE, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
