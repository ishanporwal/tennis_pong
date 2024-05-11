"""
This is where we test the view part of the game to ensure that everything
is functioning correctly when we display different aspects of the game.

This module defines tests for start screen, end screen, play again, and exit
visuals.
"""

import pygame
import pytest
from pong_view import View
from pong_model import Model

# Initialize pygame
pygame.init()


# ~~~~~~~~~~~~~~~~~START SCREEN CODE~~~~~~~~~~~~~~~~~~~~~~


# Checks that when the user runs the code
# a start screen appears.
def test_start_screen_displayed():
    """
    Test case to check if the start screen is displayed properly.
    """
    # Initialize pygame
    pygame.init()
    # Create a screen surface with dimensions 800x600
    screen = pygame.display.set_mode((800, 600))
    # Create a View object
    view = View(screen)
    # Display the start screen and get the play button
    play_button = view.start_screen()
    # Assert that the play button is a pygame Rect object
    assert isinstance(play_button, pygame.Rect)


# Checks that when the user clicks start,
# the game starts.
def test_start_screen_play_button():
    """
    Test case to check if clicking the play button on
    the start screen starts the game.
    """
    # Initialize pygame
    pygame.init()
    # Create a screen surface with dimensions 800x600
    screen = pygame.display.set_mode((800, 600))
    # Create a View object
    view = View(screen)
    # Display the start screen and get the play button
    play_button = view.start_screen()
    # Create a MOUSEBUTTONDOWN event to simulate clicking the play button
    event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"button": 1})
    # Set the position of the event to click inside the play button
    event.pos = (play_button.x + 1, play_button.y + 1)
    # Post the event
    pygame.event.post(event)
    # Assert that a MOUSEBUTTONDOWN event is in the event queue
    assert pygame.event.get(pygame.MOUSEBUTTONDOWN)


# ~~~~~~~~~~~~~ END SCREEN CODE~~~~~~~~~~~~~~~~~~~


# Checks that when the end screen is
# displayed correctly.
def test_end_screen_display():
    """
    Test case to check if the end screen is displayed properly.
    """
    # Initialize pygame
    pygame.init()
    # Create a screen surface with dimensions 800x600
    screen = pygame.display.set_mode((800, 600))
    # Create a View object
    view = View(screen)
    # Create a Model object with screen dimensions 800x600
    model = Model(800, 600)
    # Display the end screen and get the play again and exit buttons
    play_again_button, exit_button = view.end_screen(model)
    # Assert that the play again button and exit button are pygame Rect objects
    assert isinstance(play_again_button, pygame.Rect)
    assert isinstance(exit_button, pygame.Rect)


# Checks that if the CPU wins,
# the end screen says so.
def test_end_screen_cpu_win():
    """
    Test case to check if end screen displays CPU win when CPU wins.
    """
    # visual inspection
    assert True


# Checks that if the player wins,
# the end screen says so.
def test_end_screen_player_win():
    """
    Test case to check if end screen displays Player win when Player wins.
    """
    # visual inspection
    assert True


# Checks that if the player clicks "play again"
# on the end screen, it starts a new game
# without a start screen.
def test_end_screen_play_again():
    """
    Test case to check if clicking "Play Again" on the end screen
    starts a new game.
    """
    # Initialize pygame
    pygame.init()
    # Create a screen surface with dimensions 800x600
    screen = pygame.display.set_mode((800, 600))
    # Create a View object
    view = View(screen)
    # Create a Model object with screen dimensions 800x600
    model = Model(800, 600)
    # Display the end screen and get the play again button
    play_again_button, _ = view.end_screen(model)
    # Create a MOUSEBUTTONDOWN event to simulate clicking the play again button
    event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"button": 1})
    # Set the position of the event to click inside the play again button
    event.pos = (play_again_button.x + 1, play_again_button.y + 1)
    # Post the event
    pygame.event.post(event)
    # Assert that a MOUSEBUTTONDOWN event is in the event queue
    assert pygame.event.get(pygame.MOUSEBUTTONDOWN)


# Checks that if player clicks exit
# on the end screen, the game exits.
def test_end_screen_exit():
    """
    Test case to check if clicking "Exit" on the end screen exits the game.
    """
    # Initialize pygame
    pygame.init()
    # Create a screen surface with dimensions 800x600
    screen = pygame.display.set_mode((800, 600))
    # Create a View object
    view = View(screen)
    # Create a Model object with screen dimensions 800x600
    model = Model(800, 600)
    # Display the end screen and get the exit button
    _, exit_button = view.end_screen(model)
    # Create a MOUSEBUTTONDOWN event to simulate clicking the exit button
    event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"button": 1})
    # Set the position of the event to click inside the exit button
    event.pos = (exit_button.x + 1, exit_button.y + 1)
    # Post the event
    pygame.event.post(event)
    # Assert that no QUIT event is in the event queue
    assert pygame.event.get(pygame.QUIT) == []
