# pong_controller.py
"""
Module for the Controller class, responsible for handling user input events
for the game.

This module defines the Controller class, which handles user input events
such as quitting the game or moving the player's racket. It contains methods
to initialize the Controller object and handle user input events.

"""

import sys
import pygame


class Controller:
    """
    Handles user input events for the game.
    """

    def __init__(self):
        """
        Initializes the Controller object.
        """

    def handle_events(self):
        """
        Handles user input events such as quitting the game or moving the
        player's racket.

        Returns:
            An int representing the amount by which to move the player's racket
            vertically.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        speed_y = 0
        if keys[pygame.K_UP]:
            speed_y = -6
        elif keys[pygame.K_DOWN]:
            speed_y = 6
        return speed_y
