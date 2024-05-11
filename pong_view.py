# view.py
"""
Module for the View class, responsible for handling the game's visual aspects.

This module defines the View class, which manages the rendering of the game
view, including graphics, text, and user interfaces. It contains methods
to render various elements such as the ball, rackets, net, score, and
start/end screens.

"""
import sys
import pygame


class View:
    """
    Handles rendering of the game view, including graphics, text, and user
    interfaces.
    """

    def __init__(self, screen):
        """
        Initializes the View object with the given screen.

        Args:
            screen: An instance of the Pygame surface class used to render
            graphics on.
        """
        self.screen = screen
        self.score_font = pygame.font.Font(None, 100)
        self.net = pygame.Rect(
            self.screen.get_width() / 2 - 5, 0, 10, self.screen.get_height()
        )
        self.player_image = pygame.image.load(
            "tennis_racket.png"
        ).convert_alpha()
        self.cpu_image = pygame.image.load("tennis_racket.png").convert_alpha()

        self.player_image = pygame.transform.scale(self.player_image, (40, 100))
        self.cpu_image = pygame.transform.scale(self.cpu_image, (40, 100))

    def render(self, model):
        """
        Renders the game view, including the ball, rackets, net, and score.

        Args:
            model: The Model object containing game state information.
        """
        self.screen.fill("dark green")
        self.score(model)
        self.court()
        self.racket(model.player.rect, self.player_image)
        self.racket(model.cpu.rect, self.cpu_image)
        pygame.draw.ellipse(self.screen, "green", model.ball.rect)
        pygame.draw.rect(self.screen, "black", self.net)
        pygame.display.update()

    def score(self, model):
        """
        Renders the current score on the game screen.

        Args:
            model: The Model object containing game state information.
        """
        cpu_score_surface = self.score_font.render(
            str(model.cpu_score), True, "white"
        )
        player_score_surface = self.score_font.render(
            str(model.player_score), True, "white"
        )
        self.screen.blit(cpu_score_surface, (self.screen.get_width() / 4, 20))
        self.screen.blit(
            player_score_surface, (self.screen.get_width() * 0.75, 20)
        )

    def court(self):
        """
        Renders the tennis court lines on the game screen.
        """
        pygame.draw.aaline(
            self.screen,
            "white",
            (self.screen.get_width() / 4, self.screen.get_height() / 8),
            (self.screen.get_width() / 4, self.screen.get_height() * 7 / 8),
        )
        pygame.draw.aaline(
            self.screen,
            "white",
            (self.screen.get_width() * 3 / 4, self.screen.get_height() / 8),
            (self.screen.get_width() * 3 / 4, self.screen.get_height() * 7 / 8),
        )
        pygame.draw.aaline(
            self.screen,
            "black",
            (self.screen.get_width() / 2, 0),
            (self.screen.get_width() / 2, self.screen.get_height()),
        )
        pygame.draw.aaline(
            self.screen,
            "white",
            (0, self.screen.get_height() / 8),
            (self.screen.get_width(), self.screen.get_height() / 8),
        )
        pygame.draw.aaline(
            self.screen,
            "white",
            (0, self.screen.get_height() * 7 / 8),
            (self.screen.get_width(), self.screen.get_height() * 7 / 8),
        )
        pygame.draw.aaline(
            self.screen,
            "white",
            (0, self.screen.get_height() / 2),
            (10, self.screen.get_height() / 2),
        )
        pygame.draw.aaline(
            self.screen,
            "white",
            (self.screen.get_width(), self.screen.get_height() / 2),
            (self.screen.get_width() - 10, self.screen.get_height() / 2),
        )
        pygame.draw.aaline(
            self.screen,
            "white",
            (self.screen.get_width() / 4, self.screen.get_height() / 2),
            (self.screen.get_width() * 3 / 4, self.screen.get_height() / 2),
        )

    def racket(self, rect, image):
        """
        Renders a racket on the game screen.

        Args:
            rect: An instance of the pygame.Rect class, which represents a
            rectangle representing the position and size of the racket.
            image: An instance of the pygame.Surface class representing
            the image of the racket.
        """
        self.screen.blit(image, rect)

    def start_screen(self):
        """
        Renders the start screen and returns the play button rectangle for
        event handling.

        Returns:
            The rectangle representing the play button in the form pygame.Rect
        """
        self.screen.fill("dark green")

        # Display game title
        title_font = pygame.font.Font(None, 100)
        title_text = title_font.render("Tennis Pong", True, "white")
        self.screen.blit(
            title_text,
            (self.screen.get_width() // 2 - title_text.get_width() // 2, 100),
        )

        # Display instructions
        instruction_font = pygame.font.Font(None, 36)
        instructions = [
            "Instructions:",
            (
                "Use the up and down arrow keys to move your racket along your"
                " baseline."
            ),
            "Try to hit the ball past your opponent.",
            "First to score 5 points wins!",
        ]
        y_offset = 300
        for instruction in instructions:
            instruction_text = instruction_font.render(
                instruction, True, "white"
            )
            self.screen.blit(
                instruction_text,
                (
                    self.screen.get_width() // 2
                    - instruction_text.get_width() // 2,
                    y_offset,
                ),
            )
            y_offset += 50

        # Draw play button
        play_button = pygame.Rect(
            self.screen.get_width() // 2 - 100,
            self.screen.get_height() // 2 + 200,
            200,
            50,
        )
        pygame.draw.rect(self.screen, (255, 0, 0), play_button)

        # Text for play button
        play_text = instruction_font.render("Play", True, "white")
        self.screen.blit(play_text, (play_button.x + 70, play_button.y + 10))

        pygame.display.flip()

        # Return button rectangle for event handling
        return play_button

    def end_screen(self, model):
        """
        Renders the end screen and returns the play again and exit button
        rectangles for event handling.

        Args:
            model: The Model object containing game state information.

        Returns:
            The rectangles representing the play again and exit buttons
            in a tuple form [pygame.Rect, pygame.Rect]
        """
        self.screen.fill("dark green")

        # Display final scores
        font = pygame.font.Font(None, 64)
        cpu_score_surface = font.render(
            "CPU Score: " + str(model.cpu_score), True, "white"
        )
        player_score_surface = font.render(
            "Player Score: " + str(model.player_score), True, "white"
        )
        self.screen.blit(
            cpu_score_surface,
            (
                self.screen.get_width() // 2 - 150,
                self.screen.get_height() // 2 - 50,
            ),
        )
        self.screen.blit(
            player_score_surface,
            (
                self.screen.get_width() // 2 - 150,
                self.screen.get_height() // 2 + 50,
            ),
        )

        if model.cpu_score > model.player_score:
            winner_surface = font.render("CPU wins!", True, "white")
        elif model.player_score > model.cpu_score:
            winner_surface = font.render("Player wins!", True, "white")
        else:
            winner_surface = font.render("It's a tie!", True, "white")
        self.screen.blit(
            winner_surface,
            (
                self.screen.get_width() // 2 - 150,
                self.screen.get_height() // 2 + 150,
            ),
        )

        # Draw buttons
        play_again_button = pygame.Rect(
            self.screen.get_width() // 2 - 150,
            self.screen.get_height() // 2 - 150,
            300,
            70,
        )
        exit_button = pygame.Rect(
            self.screen.get_width() // 2 - 150,
            self.screen.get_height() // 2 - 250,
            300,
            70,
        )
        pygame.draw.rect(self.screen, (255, 0, 0), play_again_button)
        pygame.draw.rect(self.screen, (255, 0, 0), exit_button)

        # Text for buttons
        play_again_text = font.render("Play Again", True, "white")
        exit_text = font.render("Exit", True, "white")
        self.screen.blit(
            play_again_text,
            (play_again_button.x + 40, play_again_button.y + 15),
        )
        self.screen.blit(exit_text, (exit_button.x + 105, exit_button.y + 15))

        pygame.display.flip()

        return play_again_button, exit_button

    def winner_end_game(self, model):
        """
        Renders the end game screen if a winner is determined, allowing
        the player to play again or exit.

        Args:
            model: The Model object containing game state information.
        """
        if model.cpu_score < 5 and model.player_score < 5:
            return

        play_again_button, exit_button = self.end_screen(model)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button != 1:
                        continue

                    mouse_pos = pygame.mouse.get_pos()
                    if play_again_button.collidepoint(mouse_pos):
                        model.cpu_score = 0
                        model.player_score = 0
                        return "play_again"
                    if exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
