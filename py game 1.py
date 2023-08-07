import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up game variables
gravity = 0.4
player_speed = 1.5
jump_height = 10
player_pos = pygame.Rect(50, HEIGHT - 100, 50, 50)
player_y_momentum = 0
player_jumping = False
platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),  # Ground platform
    pygame.Rect(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),  # Middle platform
    pygame.Rect(WIDTH - 100, HEIGHT / 2, 100, 20),  # Right platform
]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not player_jumping:
                player_y_momentum -= jump_height
                player_jumping = True

    # Apply gravity
    player_y_momentum += gravity

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos.x += player_speed

    player_pos.y += player_y_momentum

    # Check for collisions
    for platform in platforms:
        if player_pos.colliderect(platform):
            if player_y_momentum > 0:
                player_pos.y = platform.y - player_pos.height
                player_y_momentum = 0
                player_jumping = False
            elif player_y_momentum < 0:
                player_pos.y = platform.y + platform.height
                player_y_momentum = 0

    # Check if the player falls off the screen
    if player_pos.y > HEIGHT:
        player_pos.y = HEIGHT - player_pos.height
        player_y_momentum = 0
        player_jumping = False

    # Clear the screen
    win.fill(WHITE)

    # Draw player
    pygame.draw.rect(win, BLUE, player_pos)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(win, RED, platform)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
