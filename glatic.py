import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_WIDTH = 40
SHIP_HEIGHT = 40
ENEMY_WIDTH = 60  # Widened enemy width
ENEMY_HEIGHT = 40
PROJECTILE_WIDTH = 10
PROJECTILE_HEIGHT = 20
HAZARD_WIDTH = 60  # Widened hazard width
HAZARD_HEIGHT = 20

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galactic Gliders")

# Game loop
def game_loop():
    ship_x = SCREEN_WIDTH // 2
    ship_y = SCREEN_HEIGHT - SHIP_HEIGHT
    ship_speed = 5

    enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
    enemy_y = 0
    enemy_speed = 3

    hazards = []
    projectiles = []
    score = 0

    machine_gun_active = False
    machine_gun_timer = 0
    y_key_down_time = 0

    clock = pygame.time.Clock()

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Fire a projectile when the space bar is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if machine_gun_active:
                    projectiles.append(
                        [ship_x + SHIP_WIDTH // 2 - PROJECTILE_WIDTH // 2, ship_y, BLACK]
                    )
                else:
                    projectiles.append([ship_x + SHIP_WIDTH // 2 - PROJECTILE_WIDTH // 2, ship_y, RED])

            # Toggle machine gun mode when "y" key is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                y_key_down_time = pygame.time.get_ticks()
            elif event.type == pygame.KEYUP and event.key == pygame.K_y:
                time_elapsed = pygame.time.get_ticks() - y_key_down_time
                if time_elapsed >= 3000:
                    machine_gun_active = not machine_gun_active

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship_x > 0:
            ship_x -= ship_speed
        if keys[pygame.K_RIGHT] and ship_x < SCREEN_WIDTH - SHIP_WIDTH:
            ship_x += ship_speed

        enemy_y += enemy_speed
        if enemy_y > SCREEN_HEIGHT:
            enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
            enemy_y = 0

        # Generate hazards
        if random.random() < 0.01:
            hazards.append([random.randint(0, SCREEN_WIDTH - HAZARD_WIDTH), 0, RED])

        # Move hazards
        for hazard in hazards[:]:
            hazard[1] += 2  # Move downwards

            # Check for collision between hazards and the ship
            if (
                hazard[0] < ship_x + SHIP_WIDTH
                and hazard[0] + HAZARD_WIDTH > ship_x
                and hazard[1] < ship_y + SHIP_HEIGHT
                and hazard[1] + HAZARD_HEIGHT > ship_y
            ):
                game_over = True

            # Check for collision between hazards and projectiles
            for projectile in projectiles[:]:
                if (
                    hazard[0] < projectile[0] + PROJECTILE_WIDTH
                    and hazard[0] + HAZARD_WIDTH > projectile[0]
                    and hazard[1] < projectile[1] + PROJECTILE_HEIGHT
                    and hazard[1] + HAZARD_HEIGHT > projectile[1]
                ):
                    hazards.remove(hazard)
                    projectiles.remove(projectile)

        # Move projectiles
        for projectile in projectiles[:]:
            projectile[1] -= 5  # Move upwards

            # Check for collisions between projectiles and enemies
            if (
                projectile[0] < enemy_x + ENEMY_WIDTH
                and projectile[0] + PROJECTILE_WIDTH > enemy_x
                and projectile[1] < enemy_y + ENEMY_HEIGHT
                and projectile[1] + PROJECTILE_HEIGHT > enemy_y
            ):
                projectiles.remove(projectile)
                score += 1

        # Check for collision with enemy
        if (
            ship_x < enemy_x + ENEMY_WIDTH
            and ship_x + SHIP_WIDTH > enemy_x
            and ship_y < enemy_y + ENEMY_HEIGHT
            and ship_y + SHIP_HEIGHT > enemy_y
        ):
            game_over = True

        # Clear the screen
        screen.fill(WHITE)

        # Draw the ship, enemy, hazards, and projectiles
        pygame.draw.rect(screen, RED, (ship_x, ship_y, SHIP_WIDTH, SHIP_HEIGHT))
        pygame.draw.rect(screen, RED, (enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT))

        for hazard in hazards:
            pygame.draw.rect(
                screen,
                hazard[2],  # Color of the hazard
                (hazard[0], hazard[1], HAZARD_WIDTH, HAZARD_HEIGHT),
            )

        for projectile in projectiles:
            pygame.draw.rect(
                screen,
                projectile[2],  # Color of the projectile
                (projectile[0], projectile[1], PROJECTILE_WIDTH, PROJECTILE_HEIGHT),
            )

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(60)

    pygame.quit()
    quit()

# Start the game loop
game_loop()
