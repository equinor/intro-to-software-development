# Much of this module is based on content from from https://realpython.com/pygame-a-primer/
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from rolling_stone.player import Player
from rolling_stone.stone import Stone

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

TOP_BAR_HEIGHT = 50

BRIGHT_YELLOW_RGB = (255, 255, 0)
DARK_GREY_RGB = (50, 50, 50)
WOOD_RGB = (161, 102, 47)


def draw_player_info(screen, player):
    font = pygame.font.Font(None, 36)
    text = font.render(
        f"Player: {player.name}, "
        f"Score: {player.score}, "
        f"Personal Best: {player.personal_best}",
        True,
        (255, 255, 255),
    )
    screen.blit(text, (10, 10))


def run_game():
    pygame.init()

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    stone = Stone()

    player = Player()
    player.prompt_for_name()

    running = True
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

        # Fill the screen with black
        screen.fill(WOOD_RGB)

        # Update the player sprite based on user keypresses
        pressed_keys = pygame.key.get_pressed()
        stone.update_speed_on_keypress(pressed_keys)
        stone.move_within_screen(SCREEN_WIDTH, SCREEN_HEIGHT, TOP_BAR_HEIGHT)

        screen.blit(stone.surf, stone.rect)

        # Draw a top bar
        pygame.draw.rect(screen, DARK_GREY_RGB, (0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT))

        # Draw the player's info on the top bar
        draw_player_info(screen, player)

        # Update the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)


if __name__ == "__main__":
    run_game()
