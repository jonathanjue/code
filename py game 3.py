import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")

# Load images
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")
weapon_img = pygame.image.load("weapon.png")

# Set up the player
player_size = player_img.get_size()
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Set up the enemy
enemy_size = enemy_img.get_size()
enemy_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
enemy_speed = 2

# Set up the weapon
weapon_size = weapon_img.get_size()
weapon_pos = [player_pos[0], player_pos[1] + player_size[1] + 10]
has_weapon = True

# Set up the bullets
bullet_size = bullet_img.get_size()
bullets = []

# Set up the game clock
clock = pygame.time.Clock()

# Function to shoot a bullet
def shoot():
    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Calculate the bullet velocity based on the player's position and the mouse position
    bullet_angle = math.atan2(mouse_pos[1] - player_pos[1], mouse_pos[0] - player_pos[0])
    bullet_speed = 10
    bullet_velocity = [bullet_speed * math.cos(bullet_angle), bullet_speed * math.sin(bullet_angle)]

    # Add the bullet to the list
    bullets.append([player_pos[0], player_pos[1], bullet_velocity[0], bullet_velocity[1]])

# Function to check collision between two circles
def check_collision(circle1_pos, circle1_radius, circle2_pos, circle2_radius):
    distance = math.sqrt((circle1_pos[0] - circle2_pos[0]) ** 2 + (circle1_pos[1] - circle2_pos[1]) ** 2)
    if distance < circle1_radius + circle2_radius:
        return True
    else:
        return False

# Game loop
running = True
survival_timer = 0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Wrap around the screen for the player
    if player_pos[0] < 0:
        player_pos[0] = WIDTH
    elif player_pos[0] > WIDTH:
        player_pos[0] = 0
    if player_pos[1] < 0:
        player_pos[1] = HEIGHT
    elif player_pos[1] > HEIGHT:
        player_pos[1] = 0

    # Move the enemy towards the player
    enemy_angle = math.atan2(player_pos[1] - enemy_pos[1], player_pos[0] - enemy_pos[0])
    enemy_speed_x = enemy_speed * math.cos(enemy_angle)
    enemy_speed_y = enemy_speed * math.sin(enemy_angle)
    enemy_pos[0] += enemy_speed_x
    enemy_pos[1] += enemy_speed_y

    # Wrap around the screen for the enemy
    if enemy_pos[0] < 0:
        enemy_pos[0] = WIDTH
    elif enemy_pos[0] > WIDTH:
        enemy_pos[0] = 0
    if enemy_pos[1] < 0:
        enemy_pos[1] = HEIGHT
    elif enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0

    # Move the bullets
    for bullet in bullets:
        bullet[0] += bullet[2]  # Update bullet x position
        bullet[1] += bullet[3]  # Update bullet y position

    # Check if bullet hits the enemy
    for bullet in bullets:
        if check_collision(bullet, bullet_size[0] / 2, enemy_pos, enemy_size[0] / 2):
            bullets.remove(bullet)

    # Check for collision with the enemy
    if check_collision(player_pos, player_size[0] / 2, enemy_pos, enemy_size[0] / 2):
        running = False

    # Check for collision with the weapon
    if check_collision(player_pos, player_size[0] / 2, weapon_pos, weapon_size[0] / 2) and not has_weapon:
        weapon_pos = [-100, -100]  # Move the weapon off-screen
        has_weapon = True

    # Increment the survival timer
    survival_timer += 1

    # Clear the screen
    win.fill((255, 255, 255))

    # Draw the player
    win.blit(player_img, (player_pos[0] - player_size[0] / 2, player_pos[1] - player_size[1] / 2))

    # Draw the enemy
    win.blit(enemy_img, (enemy_pos[0] - enemy_size[0] / 2, enemy_pos[1] - enemy_size[1] / 2))

    # Draw the bullets
    for bullet in bullets:
        win.blit(bullet_img, (bullet[0] - bullet_size[0] / 2, bullet[1] - bullet_size[1] / 2))

    # Draw the weapon if it hasn't been picked up
    if not has_weapon:
        win.blit(weapon_img, (weapon_pos[0] - weapon_size[0] / 2, weapon_pos[1] - weapon_size[1] / 2))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)

# Quit the game
pygame.quit()
