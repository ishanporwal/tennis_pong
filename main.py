# main.py
"""
Main module for the Tennis Pong game.

This module initializes the game, creates instances of the Model, View,
and Controller classes,and contains the main game loop. It handles event
processing, user input, and rendering of the game view.

"""
import pygame
from pong_model import Model
from pong_view import View
from pong_controller import Controller

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tennis Pong")

# Create a Pygame clock object to control the frame rate
clock = pygame.time.Clock()

# Create instances of the Model, View, and Controller classes
model = Model(SCREEN_WIDTH, SCREEN_HEIGHT)
view = View(screen)
controller = Controller()

# Display the start screen and wait for the player to click the play button
play_button = view.start_screen()
GAME_RUNNING = False

# Main game loop
while True:
    # Event handling loop
    for event in pygame.event.get():
        # Check if the user quits the game
        if event.type == pygame.QUIT:
            model.quit_game()
        # Check if the user clicks the play button on the start screen
        elif event.type == pygame.MOUSEBUTTONDOWN and not GAME_RUNNING:
            if event.button == 1 and play_button.collidepoint(event.pos):
                GAME_RUNNING = True  # Start the game

    # If the game is running
    if GAME_RUNNING:
        # Handle user input and move game objects
        KEYS_PRESSED = controller.handle_events()
        model.move_objects()
        model.move_player(KEYS_PRESSED)
        model.move_cpu()

        # Render the game view
        view.render(model)
        view.winner_end_game(model)
    else:
        # If the game is not running, display the start screen
        play_button = view.start_screen()

    # Control frame rate
    clock.tick(60)
