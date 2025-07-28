import pygame
from config import WHITE

class Wormhole:
    def __init__(self, x, y, radius=40, color=(180, 0, 255), destination=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.position = pygame.Vector2(x, y)
        self.destination = destination
        self.ship_was_inside = True  # State tracking

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, width=4)
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius - 10, width=2)

    def check_entry(self, spaceship_rect):
        """
        Call this every frame to check if the ship just entered the wormhole.
        Returns True only when the ship crosses from outside to inside.
        """
        spaceship_center = spaceship_rect.center
        distance = pygame.Vector2(spaceship_center).distance_to(self.position)
        inside_now = distance < self.radius

        just_entered = inside_now and not self.ship_was_inside
        self.ship_was_inside = inside_now

        return just_entered
