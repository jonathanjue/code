import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Defender")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player spaceship
player_img = pygame.image.load("spaceship.png")
player_rect = player_img.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10
player_speed = 1

# Enemy spaceship
enemy_img = pygame.image.load("enemy for cosmic defenders.jpg")
enemy_rect = enemy_img.get_rect()
enemy_speed = 2
enemy_spawn_delay = 1000
last_spawn_time = pygame.time.get_ticks()

# Bullets
bullet_img = pygame.image.load("bullet.png")
bullet_rect = bullet_img.get_rect()
bullet_speed = 5
bullet_state = "ready"

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    window.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += player_speed

    # Enemy spawning
    now = pygame.time.get_ticks()
    if now - last_spawn_time >= enemy_spawn_delay:
        enemy_rect.x = random.randint(0, WIDTH - enemy_rect.width)
        enemy_rect.y = 0
        last_spawn_time = now

    # Move enemy
    enemy_rect.y += enemy_speed

    # Bullet movement
    if bullet_state == "fire":
        bullet_rect.y -= bullet_speed
        if bullet_rect.y <= 0:
            bullet_state = "ready"

    # Collisions
    if bullet_rect.colliderect(enemy_rect):
        bullet_state = "ready"
        score += 1
        enemy_rect.y = -enemy_rect.height

    # Draw sprites
    window.blit(player_img, player_rect)
    window.blit(enemy_img, enemy_rect)
    if bullet_state == "fire":
        window.blit(bullet_img, bullet_rect)

    # Draw score
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
