import pygame
import os
from config import SHIP_SPEED, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        # Load spaceship image using a relative path
        base_dir = os.path.dirname(os.path.dirname(__file__))  # Go to project root
        image_path = os.path.join(base_dir, "assets", "images", "SpaceShip", "Spaceship_tut.png")
        raw_image = pygame.image.load(image_path).convert_alpha()

        # Optional: scale the ship image
        self.original_image = pygame.transform.smoothscale(raw_image, (60, 50))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=self.position)

        self.angle = 0  # For rotation, if desired

    def handle_input(self, keys):
        self.velocity.x = 0
        self.velocity.y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity.x = -SHIP_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity.x = SHIP_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity.y = -SHIP_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity.y = SHIP_SPEED

    def shortest_angle_diff(current, target):
        diff = (target - current + 180) % 360 - 180
        return diff

    def update(self):
        self.position += self.velocity
        self.position.x = max(0, min(SCREEN_WIDTH, self.position.x))
        self.position.y = max(0, min(SCREEN_HEIGHT, self.position.y))

        # Update rect center
        self.rect.center = self.position

        # Optional: rotate image to face movement
        if self.velocity.length_squared() > 0:

            #self.angle = self.velocity.angle_to(pygame.Vector2(0, -1))  # Instant Rotate

            target_angle = self.velocity.angle_to(pygame.Vector2(0, -1))
            angle_diff = (target_angle - self.angle + 180) % 360 - 180
            #angle_diff = shortest_angle_diff(self.angle, target_angle)
            self.angle += angle_diff * 0.2  # Smooth rotation

            # Keep angle within [0, 360)
            self.angle %= 360

            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.position)
        else:
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


