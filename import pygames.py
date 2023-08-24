import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Space Invaders")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
light_blue = (173, 216, 230)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Clock for FPS
clock = pygame.time.Clock()

# Player spaceship properties
spaceship_width = 50
spaceship_height = 50
spaceship_x = display_width // 2 - spaceship_width // 2
spaceship_y = display_height - spaceship_height - 10
spaceship_speed = 5

# Green square properties
green_square_size = 60  # Increased size
green_square_speed = 3
green_squares = []
green_square_cooldown = 60
green_square_timer = green_square_cooldown
green_square_speed_multiplier = 1  # Speed multiplier for green squares
green_square_speed_increase_timer = 300  # 5 seconds
green_square_speed_increase_counter = 0

# Boss properties
boss_width = 100
boss_height = 100
boss_x = display_width // 2 - boss_width // 2
boss_y = 50
boss_health = 100

# Life bar properties
life_bar_width = 200
life_bar_height = 20
life_bar_x = display_width // 2 - life_bar_width // 2
life_bar_y = 30
life_bar_value = 100

# Score properties
score = 0
score_font = pygame.font.Font(None, 36)

# Bullet properties
bullet_width = 15
bullet_height = 30
bullet_color = red
bullet_speed = 7
bullets = []

# Level properties
current_level = 1
yellow_square_size = 60
yellow_square_speed = 2
yellow_squares = []
yellow_square_cooldown = 120
yellow_square_timer = yellow_square_cooldown
level_duration = 0
level_start_time = pygame.time.get_ticks()

# Pause flag
paused = False

# Main menu
def main_menu():
    global current_level
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if current_level == 1:
                        game_loop()
                    elif current_level == 2:
                        game_loop(level=2)

        game_display.fill(light_blue)
        menu_font = pygame.font.Font(None, 72)
        menu_text = menu_font.render("Main Menu", True, black)
        level_text = pygame.font.Font(None, 36).render("Press ENTER to start Level " + str(current_level), True, black)
        game_display.blit(menu_text, (display_width // 2 - 150, display_height // 2 - 50))
        game_display.blit(level_text, (display_width // 2 - 180, display_height // 2 + 50))
        pygame.display.update()
        clock.tick(15)

# Toggle the green square speed multiplier
def toggle_green_square_speed():
    global green_square_speed_multiplier
    green_square_speed_multiplier = 2 if green_square_speed_multiplier == 1 else 1

# Main game loop
def game_loop(level=1):
    global spaceship_x, spaceship_speed, green_squares, green_square_timer, life_bar_value, score, bullets, boss_health
    global yellow_squares, yellow_square_timer, level_duration, level_start_time
    global green_square_speed_multiplier, green_square_speed_increase_counter, paused

    game_exit = False
    move_left = False
    move_right = False
    speed_up = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            # Check for key press events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_UP:
                    speed_up = True
                elif event.key == pygame.K_ESCAPE:
                    paused = not paused

            # Check for key release events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_UP:
                    speed_up = False

            # Check for mouse events
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                bullets.append({'x': spaceship_x + spaceship_width // 2 - bullet_width // 2,
                                'y': spaceship_y - bullet_height})

        # Pause the game if needed
        if paused:
            pygame.display.set_caption("Space Invaders - Paused")
            continue
        else:
            pygame.display.set_caption("Space Invaders")

        # Toggle green square speed
        if speed_up:
            toggle_green_square_speed()

        # Move the spaceship
        if move_left:
            spaceship_x -= spaceship_speed
        if move_right:
            spaceship_x += spaceship_speed

        # Clear the display
        game_display.fill(light_blue)

        # Draw the spaceship
        pygame.draw.rect(game_display, black, [spaceship_x, spaceship_y, spaceship_width, spaceship_height])

        # Update and draw the green squares
        for square in green_squares:
            square['y'] += green_square_speed * green_square_speed_multiplier

            # Check for collision with the spaceship
            if (spaceship_x < square['x'] + green_square_size and
                    spaceship_x + spaceship_width > square['x'] and
                    spaceship_y < square['y'] + green_square_size and
                    spaceship_y + spaceship_height > square['y']):
                if square['color'] == green:
                    life_bar_value -= 20  # Reduce the life bar value
                square['color'] = blue

            pygame.draw.rect(game_display, square['color'], [square['x'], square['y'], green_square_size, green_square_size])

        # Update and draw the boss
        pygame.draw.rect(game_display, yellow, [boss_x, boss_y, boss_width, boss_height])

        # Update and draw the life bar
        pygame.draw.rect(game_display, black, [life_bar_x, life_bar_y, life_bar_width, life_bar_height])
        pygame.draw.rect(game_display, green, [life_bar_x, life_bar_y,
                                                (life_bar_value / 100) * life_bar_width, life_bar_height])

        # Check if life bar is empty
        if life_bar_value <= 0:
            game_over()

        # Update and draw the score
        score_text = score_font.render("Score: " + str(score), True, black)
        game_display.blit(score_text, (10, 10))

        # Generate new green square
        green_square_timer -= 1
        if green_square_timer <= 0:
            green_squares.append({'x': random.randint(0, display_width - green_square_size),
                                  'y': 0 - green_square_size,
                                  'color': green})
            green_square_timer = green_square_cooldown

        # Update and draw the bullets
        for bullet in bullets:
            bullet['y'] -= bullet_speed
            pygame.draw.rect(game_display, bullet_color, [bullet['x'], bullet['y'], bullet_width, bullet_height])

            # Check for collision with the boss
            if (bullet['x'] > boss_x and bullet['x'] < boss_x + boss_width and
                    bullet['y'] > boss_y and bullet['y'] < boss_y + boss_height):
                bullets.remove(bullet)
                boss_health -= 10
                if boss_health <= 0:
                    score += 100
                    boss_health = 100

        # Update and draw the boss health bar
        pygame.draw.rect(game_display, black, [boss_x, boss_y - 20, boss_width, 10])
        pygame.draw.rect(game_display, red, [boss_x, boss_y - 20, (boss_health / 100) * boss_width, 10])

        # Update and draw the yellow squares for level 2
        if level == 2:
            for square in yellow_squares:
                square['y'] += yellow_square_speed

                # Check for collision with the spaceship
                if (spaceship_x < square['x'] + yellow_square_size and
                        spaceship_x + spaceship_width > square['x'] and
                        spaceship_y < square['y'] + yellow_square_size and
                        spaceship_y + spaceship_height > square['y']):
                    life_bar_value -= 30  # Reduce the life bar value

                pygame.draw.rect(game_display, yellow, [square['x'], square['y'], yellow_square_size, yellow_square_size])

            # Generate new yellow square
            yellow_square_timer -= 1
            if yellow_square_timer <= 0:
                yellow_squares.append({'x': random.randint(0, display_width - yellow_square_size),
                                       'y': 0 - yellow_square_size})
                yellow_square_timer = yellow_square_cooldown

            # Check for level duration and switch to main menu or level completion
            level_duration = (pygame.time.get_ticks() - level_start_time) // 1000
            if level == 2 and level_duration >= 20:  # Adjust time as needed
                level_complete()

        # Update the display
        pygame.display.update()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    quit()

# Function to end the game
def game_over():
    global game_display

    game_display.fill(white)
    game_over_text = pygame.font.Font(None, 72).render("Game Over", True, black)
    game_display.blit(game_over_text, (display_width // 2 - 150, display_height // 2 - 50))
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 1 second before quitting the game

    pygame.quit()
    quit()

# Function for level completion
def level_complete():
    global current_level

    game_display.fill(white)
    level_complete_text = pygame.font.Font(None, 72).render("Level " + str(current_level) + " Complete!", True, black)
    game_display.blit(level_complete_text, (display_width // 2 - 250, display_height // 2 - 50))
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 2 seconds before returning to main menu

    current_level += 1
    main_menu()

# Start the game
main_menu()