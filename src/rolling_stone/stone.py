# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP

STONE_GREY_RGB = (136, 140, 141)

MAX_SPEED = 20
SPEED_INCREMENT = 1


class Stone(pygame.sprite.Sprite):
    def __init__(self):
        super(Stone, self).__init__()
        self.surf = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.surf, STONE_GREY_RGB, (25, 25), 25)
        self.rect = self.surf.get_rect()
        self.horizontal_speed = 0
        self.vertical_speed = 0

    def update_speed_on_keypress(self, pressed_keys):
        if pressed_keys[K_UP] and self.vertical_speed < MAX_SPEED:
            self.vertical_speed += SPEED_INCREMENT
        if pressed_keys[K_DOWN] and self.vertical_speed > -MAX_SPEED:
            self.vertical_speed -= SPEED_INCREMENT
        if pressed_keys[K_LEFT] and self.horizontal_speed > -MAX_SPEED:
            self.horizontal_speed -= SPEED_INCREMENT
        if pressed_keys[K_RIGHT] and self.horizontal_speed < MAX_SPEED:
            self.horizontal_speed += SPEED_INCREMENT

    def move_within_screen(self, screen_width, screen_height, top_bar_height):
        self.rect.move_ip(self.horizontal_speed, -self.vertical_speed)

        if self.rect.left < 0:
            self.rect.left = 0
            self.horizontal_speed = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            self.horizontal_speed = 0
        if self.rect.top <= top_bar_height:
            self.rect.top = top_bar_height
            self.vertical_speed = 0
        elif self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.vertical_speed = 0
