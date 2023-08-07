import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Sandbox Game")

# Colors
white = (244, 50, 125)
black = (0, 0, 0)

# Object class
class GameObject:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(game_display, self.color, (self.x, self.y, 20, 20))

# List to store objects
objects = []

# Game loop
game_exit = False
clock = pygame.time.Clock()

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        # Add new object on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            new_object = GameObject(mouse_pos[0], mouse_pos[1], random.choice([white, black]))
            objects.append(new_object)

    # Clear the display
    game_display.fill(white)

    # Draw objects
    for obj in objects:
        obj.draw()

    # Update the display
    pygame.display.update()
    clock.tick(60)
# Quit the game
pygame.quit()
