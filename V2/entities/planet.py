import pygame
import os
from config import WHITE
from entities.stellar_object import StellarObject

class Planet(StellarObject):
    def __init__(
        self,
        orbit_center,
        orbit_radius,
        image_index=0,
        name="Planet",
        radius=50,
        orbit_angle=0.0,
        orbit_angular_speed=0.01,
        orbit_radius_change=0.0,
        rotation_speed=0.1,
    ):
        super().__init__(orbit_center, orbit_radius, orbit_angle, orbit_angular_speed, orbit_radius_change)

        self.name = name
        self.radius = radius
        self.rotation_speed = rotation_speed
        self.angle = 0  # for image rotation

        # Dynamically construct path to assets folder (relative to this file)
        base_dir = os.path.dirname(os.path.dirname(__file__))  # Go to project root
        image_path = os.path.join(base_dir, "assets", "images", "Planets", "WithShade", f"PlanetSmall ({image_index}).png")

        # Load and scale planet image
        raw_image = pygame.image.load(image_path).convert_alpha()
        scaled_size = (radius * 2, radius * 2)
        self.original_image = pygame.transform.smoothscale(raw_image, scaled_size)
        self.image = self.original_image.copy()

        # Create rect for drawing
        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        # Update orbit
        self.update_orbit_position()

        # Update self-rotation
        self.angle = (self.angle + self.rotation_speed) % 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        font = pygame.font.SysFont(None, 18)
        name_surface = font.render(self.name, True, WHITE)
        screen.blit(name_surface, (self.position.x - name_surface.get_width() // 2, self.position.y - self.radius - 20))

    def get_collision_circle(self):
        return pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            self.radius * 2,
            self.radius * 2,
        )
