import pygame
import math
from abc import ABC, abstractmethod

class StellarObject(ABC):
    def __init__(self, orbit_center, orbit_radius, orbit_angle=0.0, orbit_angular_speed=0.01, orbit_radius_change=0.0):
        self.orbit_center = pygame.Vector2(orbit_center)
        self.orbit_radius = orbit_radius
        self.orbit_angle = orbit_angle
        self.orbit_angular_speed = orbit_angular_speed
        self.orbit_radius_change = orbit_radius_change

        # Initialize position based on orbit
        self.update_orbit_position()

    def update_orbit_position(self):
        # Update orbit radius (if needed)
        self.orbit_radius += self.orbit_radius_change

        # Update angle
        self.orbit_angle += self.orbit_angular_speed

        # Compute new position
        self.position = pygame.Vector2(
            self.orbit_center.x + self.orbit_radius * math.cos(self.orbit_angle),
            self.orbit_center.y + self.orbit_radius * math.sin(self.orbit_angle)
        )

    @abstractmethod
    def update(self):
        """
        Child classes must implement this to define update behavior.
        Should include call to self.update_orbit_position().
        """
        pass

    @abstractmethod
    def draw(self, screen):
        """
        Child classes must implement how they are drawn to the screen.
        """
        pass
