# model.py
"""
Module for the Model class, responsible for managing game state and logic.

This module defines the Model class, which represents the game model for
a Pong-like game.
It contains the Ball and Racket classes, which represent the ball object
and the player and CPU rackets, respectively.
The Model class manages the game state, including the positions of game
objects, scoring, and collision detection.

"""
import random
import sys
import pygame


class Ball:
    """
    Represents a ball object in the game.

    Attributes:
        screen_width: An int representing the width of the game screen.
        screen_height: An int representing the height of the game screen.
        speed_x: An int representing the horizontal speed of the ball.
        speed_y: An int representing the vertical speed of the ball.
        rect: An instance of the pygame.Rect class, which represents a
            rectangle representing the position and size of the racket.
    """

    def __init__(self, screen_width, screen_height):
        """
        Initializes a new ball object with given screen width and height.

        Args:
            screen_width: An int representing The width of the game screen.
            screen_height: An int representing the height of the game screen.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed_x = 6
        self.speed_y = 6
        self.rect = pygame.Rect(
            self.screen_width / 2, self.screen_height / 2, 20, 20
        )
        self.reset()

    def reset(self):
        """
        Resets the position and speed of the ball.
        """
        self.rect.x = self.screen_width / 2 - 10
        self.rect.y = random.randint(10, self.screen_height - 10)
        self.speed_x = random.choice([-1, 1]) * abs(self.speed_x)
        self.speed_y = random.choice([-1, 1]) * abs(self.speed_y)

    def move(self):
        """
        Moves the ball based on its current speed.
        """
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce_vertical(self):
        """
        Moves the ball based on its current speed.
        """
        self.speed_y *= -1

    def bounce_horizontal(self):
        """
        Reverses and increases the horizontal direction of the ball.
        """
        self.speed_x *= -1.002


class Racket:
    """
    Represents a racket object in the game.

    Attributes:
        rect: An instance of the pygame.Rect class, which represents a
            rectangle representing the position and size of the racket.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Initializes a new racket object with the given position.

        Args:
            x_coordinate: An int representing the x-coordinate of the
            top-left corner of the racket.
            y_coordinate: An int representing the y-coordinate of the
            top-left corner of the racket.
        """
        self.rect = pygame.Rect(x_coordinate, y_coordinate, 20, 100)

    def move(self, speed_y):
        """
        Moves the racket vertically by the specified amount.

        Args:
            speed_y: An int representing the amount by which to move the racket
            vertically.
        """
        self.rect.y += speed_y


class Model:
    """
    Represents the game model for a Pong-like game.

    Attributes:
        screen_width: An int representing the width of the game screen.
        screen_height: An int representing the height of the game screen.
        ball: The ball object in the game.
        cpu: The CPU-controlled racket object.
        player: The player-controlled racket object.
        cpu_score: The score of the CPU.
        player_score: The score of the player.
    """

    def __init__(self, screen_width, screen_height):
        """
        Initializes a new game model with the given screen dimensions.

        Args:
            screen_width: An int representing the width of the game screen.
            screen_height: An int representing the height of the game screen.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = Ball(screen_width, screen_height)
        self.cpu = Racket(0, screen_height / 2 - 50)
        self.player = Racket(screen_width - 50, screen_height / 2 - 50)
        self.cpu_score = 0
        self.player_score = 0

    def move_objects(self):
        """
        Moves the objects in the game and handles collisions and scoring.
        """
        self.ball.move()
        if self.ball.rect.colliderect(
            self.cpu.rect
        ) or self.ball.rect.colliderect(self.player.rect):
            self.ball.bounce_horizontal()
        if (
            self.ball.rect.bottom >= self.screen_height
            or self.ball.rect.top <= 0
        ):
            self.ball.bounce_vertical()
        if self.ball.rect.right >= self.screen_width:
            self.cpu_score += 1
            self.ball.reset()
        if self.ball.rect.left <= 0:
            self.player_score += 1
            self.ball.reset()

    def move_player(self, speed_y):
        """
        Moves the player's racket vertically and ensures it stays within
        the screen bounds.

        Args:
            speed_y: An int representing the amount by which to move the
            player's racket vertically.
        """
        self.player.move(speed_y)
        self.player.rect.top = max(self.player.rect.top, 0)
        self.player.rect.bottom = min(
            self.player.rect.bottom, self.screen_height
        )

    def move_cpu(self):
        """
        Moves the CPU's racket vertically to track the ball's position.
        """
        if self.ball.rect.centery < self.cpu.rect.centery:
            self.cpu.rect.y -= 5.5
        elif self.ball.rect.centery > self.cpu.rect.centery:
            self.cpu.rect.y += 5.5

    def quit_game(self):
        """
        Quit the game.
        """
        pygame.quit()
        sys.exit()
