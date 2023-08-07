import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Top-Down Shooter")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Set up the player
player_pos = [width // 2, height // 2]
player_size = 50

# Set up the bullets
bullet_radius = 5
bullet_speed = 10
bullets = []

# Set up the walls
walls = [
    pygame.Rect(0, 0, 10, height),
    pygame.Rect(0, 0, width, 10),
    pygame.Rect(0, height - 10, width, 10),
    pygame.Rect(width - 10, 0, 10, height),
]

# Game loop
running = True
shooting = False  # Variable to track if shooting is active
sprinting = False  # Variable to track if sprinting is active
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shooting = True
            elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                sprinting = not sprinting
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shooting = False

    # Move the player with arrow keys
    keys = pygame.key.get_pressed()
    player_speed = 3
    if sprinting:
        player_speed *= 2  # Double the player's speed when sprinting
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Check for collisions between the player and the walls
    for wall in walls:
        if wall.colliderect(pygame.Rect(player_pos[0] - player_size, player_pos[1] - player_size, player_size * 2, player_size * 2)):
            # Adjust the player's position to prevent going through walls
            if player_pos[0] < wall.left:
                player_pos[0] = wall.left - player_size
            elif player_pos[0] > wall.right:
                player_pos[0] = wall.right + player_size
            if player_pos[1] < wall.top:
                player_pos[1] = wall.top - player_size
            elif player_pos[1] > wall.bottom:
                player_pos[1] = wall.bottom + player_size

    # Shoot constant bullets when the space bar is held
    if shooting:
        mouse_pos = pygame.mouse.get_pos()
        bullet_vector = [mouse_pos[0] - player_pos[0], mouse_pos[1] - player_pos[1]]
        bullets.append([list(player_pos), bullet_vector])  # No need to track bounces anymore

    # Move the bullets and check for collisions with walls
    for bullet in bullets:
        bullet[0][0] += bullet[1][0] * bullet_speed
        bullet[0][1] += bullet[1][1] * bullet_speed

        # Check for collisions with walls
        for wall in walls:
            if wall.collidepoint(bullet[0]):
                # Remove the bullet if it hits a wall
                bullets.remove(bullet)
                break

    # Draw the game objects
    window.fill(WHITE)
    pygame.draw.circle(window, GREEN, player_pos, player_size)

    for bullet in bullets:
        pygame.draw.circle(window, YELLOW, bullet[0], bullet_radius)

    for wall in walls:
        pygame.draw.rect(window, RED, wall)

    # Update the display
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Quit the game
pygame.quit()
