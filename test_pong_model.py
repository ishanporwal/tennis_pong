"""
This is where we test the model part of the game to
ensure everything is functioning correctly.
"""

import pygame
import pytest
from pong_model import Ball, Racket, Model

pygame.init()


# ~~~~~~~~~~~~~~MAIN GAME TESTS~~~~~~~~~~~~~~~~~~~~
@pytest.fixture
def model():
    """
    Helper function for creating an instance of a model.

    Returns:
        Model: An instance of the game model class.
    """
    return Model(800, 600)


# Checks that pressing the up arrow makes the
# players racket move up.
def test_move_player_racket_up(model):
    """
    Check that the player's racket moves
    up when the up key is pressed.

    Args:
        model: an instance of the game model class.
    """
    # create a racket for the player
    player = model.player
    # save the current position
    original_y = player.rect.y
    # move the players racket up 10
    # this simulates pressing the up key
    model.move_player(-10)
    # assert that the new position is 10 pixels higher than the old position.
    assert player.rect.y == original_y - 10


# Checks that pressing the down arrow makes the
# players racket move down.
def test_move_player_racket_down(model):
    """
    Check that the player's racket moves
    down when the down key is pressed.

    Args:
        model: an instance of the game model class.
    """

    # create a racket for the player
    player = model.player
    # save the current position
    original_y = player.rect.y
    # move the players racket down 10
    # this simulates pressing the down key
    model.move_player(10)  # Simulate pressing down key
    # assert that the new position is 10 pixels lower than the old position.
    assert player.rect.y == original_y + 10


# Checks that if the ball hits the left edge
# the players score increases by +1.
def test_ball_hits_left_edge(model):
    """
    Check that the player's score increases when the ball hits the left edge.

    Args:
        model: an instance of the game model class.
    """
    # create a ball instance
    ball = model.ball
    # set players's score to 0
    model.player_score = 0
    # Simulate hitting the left edge of the screen
    ball.rect.x = -10
    model.move_objects()
    # Assert that the player's score is now 1.
    assert model.player_score == 1


# Checks that if the ball hits the right edge
# the cpu's score increases by +1.
def test_ball_hits_right_edge(model):
    """
    Check if the cpu's score increases when the ball hits the right edge.

    Args:
        model: an instance of the game model class.
    """
    # create a ball instance
    ball = model.ball
    # set cpu's score to 0
    model.cpu_score = 0
    # simulate hitting the right side of the screen
    ball.rect.x = model.screen_width + 10
    model.move_objects()
    # Assert that the cpu's score is now 1.
    assert model.cpu_score == 1


# Checks that if the cpu or player score is 5,
# the game ends.
def test_game_end():
    """
    Test case to check if the game ends when either player reaches 5 points.
    """
    # Create a testing model
    game_end_model = Model(100, 100)
    # Note: this model has a smaller screen for easier testing.

    # Simulate the CPU scoring 5 times
    # ~~~~~~~~~~~~~CPU WINS~~~~~~~~~~~~~~~~~~~~~~~
    for _ in range(5):
        # Game shouldn't end in first 4 games
        assert not (
            game_end_model.cpu_score == 5 or game_end_model.player_score == 5
        )
        game_end_model.cpu_score += 1
        game_end_model.move_objects()

    # After 5 CPU scores, the game should end
    assert game_end_model.cpu_score == 5
    assert game_end_model.player_score == 0

    # Reset scores and ball position
    game_end_model.cpu_score = 0
    game_end_model.player_score = 0
    game_end_model.ball.reset()

    # ~~~~~~~~~~~~~~~~~PLAYER WINS~~~~~~~~~~~~~~~~~~~~
    # Simulate the player scoring 5 times
    for _ in range(5):
        # Game shouldn't end in first 4 games
        assert not (
            game_end_model.cpu_score == 5 or game_end_model.player_score == 5
        )
        game_end_model.player_score += 1
        game_end_model.move_objects()

    # After 5 player scores, the game should end
    assert game_end_model.cpu_score == 0
    assert game_end_model.player_score == 5


# Check that the ball stays in screen.
def test_ball_stays_in_screen(model):
    """
    Test case to check if the ball stays within the screen boundaries.

    Args:
        model: an instance of the game model class.
    """
    # create a ball instance
    ball = model.ball

    # Move the ball to the top-left corner
    ball.rect.x = 0
    ball.rect.y = 0

    # Start moving the ball to the left edge of the screen
    ball.speed_x = -6
    ball.speed_y = 0
    model.move_objects()

    # Assert ball stays within the screen width
    assert 0 <= ball.rect.x <= model.screen_width
    # Assert ball stays within the screen height
    assert 0 <= ball.rect.y <= model.screen_height

    # Move the ball to the top edge of the screen
    ball.speed_x = 0
    ball.speed_y = -6
    model.move_objects()
    # Ball should stay within the screen width
    assert 0 <= ball.rect.x <= model.screen_width
    # Ball should stay within the screen height
    assert 0 <= ball.rect.y <= model.screen_height

    # Move the ball to the bottom-right corner
    ball.rect.x = model.screen_width - ball.rect.width
    ball.rect.y = model.screen_height - ball.rect.height

    # Move the ball to the right edge of the screen
    ball.speed_x = 6
    ball.speed_y = 0
    model.move_objects()
    # Ball should stay within the screen width
    assert 0 <= ball.rect.x <= model.screen_width
    # Ball should stay within the screen height
    assert 0 <= ball.rect.y <= model.screen_height
    # Move the ball to the bottom edge of the screen
    ball.speed_x = 0
    ball.speed_y = 6
    model.move_objects()
    # Ball should stay within the screen width
    assert 0 <= ball.rect.x <= model.screen_width
    # Ball should stay within the screen height
    assert 0 <= ball.rect.y <= model.screen_height


# Checks that when the ball is reset, it is in the middle
# of the screen (x-axis) and the ball has a speed.
def test_ball_reset(model):
    """
    Test the behavior of resetting the ball in the game model.

    This function checks whether the ball is positioned
    in the middle of the screen on the x-axis and whether the
    ball has a non-zero speed after being reset.

    Args:
        model: an instance of the game model class.
    """
    ball = model.ball
    ball.reset()
    assert ball.rect.x == 390
    assert 10 <= ball.rect.y <= 590
    assert ball.speed_x != 0
    assert ball.speed_y != 0


# Checks that when we move the ball it
# is not in its original place (ensure it moves).
def test_ball_move(model):
    """
    Test the movement of the ball in the game model.

    This function checks whether the ball has moved from its
    original position after calling the move method.

    Args:
        model: an instance of the game model class.
    """
    ball = model.ball
    original_x = ball.rect.x
    original_y = ball.rect.y
    ball.move()
    assert ball.rect.x != original_x
    assert ball.rect.y != original_y


# Checks if the ball hits the top or bottom of the screen,
# it bounces off vertically.
def test_ball_bounce_vertical(model):
    """
    Test the vertical bouncing behavior of the ball in the game model.

    This function checks whether the ball's vertical speed is
    inverted after calling the bounce_vertical method.

    Args:
        model: an instance of the game model class.
    """
    ball = model.ball
    original_speed_y = ball.speed_y
    ball.bounce_vertical()
    assert ball.speed_y == -original_speed_y


# Checks if the ball hits the paddle
# it bounces off horizontally.
def test_ball_bounce_horizontal(model):
    """
    Test the horizontal bouncing behavior of the ball when
    colliding with the paddle.

    This function checks whether the ball's horizontal speed
    is inverted after calling the bounce_horizontal method.

    Args:
        model: an instance of the game model class.
    """
    ball = model.ball
    original_speed_x = ball.speed_x
    ball.bounce_horizontal()
    if ball.speed_x > 0:
        assert ball.speed_x >= int(-1 * int(original_speed_x))
    if ball.speed_x < 0:
        assert ball.speed_x <= int(-1 * int(original_speed_x))


# Checks that the paddle moves down.
def test_racket_move_down():
    """
    Test the downward movement of the racket in the game model.

    This function checks whether the racket's position has been
    correctly adjusted downwards after calling the move method.

    Returns:
        None
    """
    # create test racket instance
    racket = Racket(0, 0)
    # save original racket location
    original_y = racket.rect.y
    # move the racket
    racket.move(10)
    # assert that the racket is 10 pixels below
    # where it was originally.
    assert racket.rect.y == original_y + 10


# Checks that the paddle moves up.
def test_racket_move_up():
    """
    Test the upward movement of the racket in the game model.

    This function checks whether the racket's position has been
    correctly adjusted upwards after calling the move method.
    """
    # create test racket instance
    racket = Racket(0, 0)
    # save original racket location
    original_y = racket.rect.y
    # move the racket
    racket.move(-10)
    # assert that the racket is 10 pixels above
    # where it was originally.
    assert racket.rect.y == original_y - 10


# Checks if we are initializing the instance correctly.
def test_model_init():
    """
    Test the initialization of the game model instance.

    This function checks whether the instance variables
    are initialized correctly.

    """
    # Create a test model with screen dimensions 800x600
    model = Model(800, 600)
    # Assert that screen dimensions are initialized correctly
    assert model.screen_width == 800
    assert model.screen_height == 600
    # Assert that the objects are initialized correctly
    assert isinstance(
        model.ball, Ball
    )  # Check if ball object is instance of Ball class
    assert isinstance(
        model.cpu, Racket
    )  # Check if CPU racket object is instance of Racket class
    assert isinstance(
        model.player, Racket
    )  # Check if player racket object is instance of Racket class
    # Assert that scores are initialized to zero
    assert model.cpu_score == 0
    assert model.player_score == 0


# Checks that the player's racket cannot move past the bounds.
def test_model_move_player(model):
    """
    Test the movement of the player's racket within the game model.

    This function checks whether the player's racket is
    constrained within the game screen boundaries.

    Args:
        model: an instance of the game model class.
    """

    # Get the player's racket from the model
    player = model.player
    # Set the initial position of the player's racket
    player.rect.y = 0
    # Test moving the player's racket upwards
    model.move_player(-10)
    assert (
        player.rect.y == 0
    )  # Assert the player's racket stays at the top boundary
    # Test moving the player's racket downwards
    model.move_player(1000)
    assert (
        player.rect.y == 500
    )  # Assert the player's racket stays at the bottom boundary


# Checks to see if the CPU racket moves
# up when the ball is above it.
def test_cpu_racket_move_up(model):
    """
    Test the behavior of the CPU racket when the ball
    is above it in the game model.

    This function checks whether the CPU racket moves
    upwards when the ball's position is above it.

    Args:
        model: an instance of the game model class.
    """
    # Get the CPU racket and ball objects from the model
    cpu = model.cpu
    ball = model.ball
    # Set the initial positions of the CPU racket and the ball
    cpu.rect.y = 300
    ball.rect.y = 200
    # Move the CPU racket based on the ball's position
    model.move_cpu()
    # Assert that the CPU racket moves upwards
    assert cpu.rect.y < 300


# Checks to see if the CPU racket moves
# down when the ball is below it.
def test_cpu_racket_move_down(model):
    """
    Test the behavior of the CPU racket when the ball is
    below it in the game model.

    This function checks whether the CPU racket moves
    downwards when the ball's position is below it.

    Args:
        model: an instance of the game model class.
    """
    # Get the CPU racket and ball objects from the model
    cpu = model.cpu
    ball = model.ball
    # Set the initial positions of the CPU racket and the ball
    cpu.rect.y = 300
    ball.rect.y = 400
    # Move the CPU racket based on the ball's position
    model.move_cpu()
    # Assert that the CPU racket moves downwards
    assert cpu.rect.y > 300
