import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FPS Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player attributes
player_pos = [WIDTH // 2, HEIGHT // 2]
player_angle = 0
player_speed = 5

# Create a surface for lighting effect
light_mask = pygame.Surface((WIDTH, HEIGHT))
light_mask.set_alpha(200)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[K_w]:
        player_pos[0] += player_speed * math.cos(player_angle)
        player_pos[1] += player_speed * math.sin(player_angle)
    if keys[K_s]:
        player_pos[0] -= player_speed * math.cos(player_angle)
        player_pos[1] -= player_speed * math.sin(player_angle)
    if keys[K_a]:
        player_pos[0] -= player_speed * math.sin(player_angle)
        player_pos[1] += player_speed * math.cos(player_angle)
    if keys[K_d]:
        player_pos[0] += player_speed * math.sin(player_angle)
        player_pos[1] -= player_speed * math.cos(player_angle)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate player angle based on mouse position
    player_angle = math.atan2(mouse_y - player_pos[1], mouse_x - player_pos[0])

    # Draw sky gradient
    pygame.draw.rect(window, (0, 0, 60), (0, 0, WIDTH, HEIGHT // 2))
    pygame.draw.rect(window, (0, 0, 0), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    # Draw reflective ground
    pygame.draw.rect(window, BLUE, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
    pygame.draw.line(window, WHITE, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2))

    # Draw lighting effect
    light_mask.fill((0, 0, 0))
    pygame.draw.circle(light_mask, (255, 255, 255), (int(player_pos[0]), int(player_pos[1])), 200)
    window.blit(light_mask, (0, 0), special_flags=BLEND_ADD)

    # Draw player
    pygame.draw.rect(window, RED, (player_pos[0] - 15, player_pos[1] - 15, 30, 30))

    # Update the display
    pygame.display.flip()

    # Regulate frame rate
    clock.tick(60)  # 60 frames per second

# Quit the game
pygame.quit()
