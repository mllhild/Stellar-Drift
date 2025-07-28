from entities.planet import Planet
from entities.wormhole import Wormhole
import pygame
import math

class SolarSystem:
    def __init__(self, name="Unnamed System", center=(800, 450)):  # default center of screen
        self.name = name
        self.center = pygame.Vector2(center)
        self.stars = []
        self.planets = []
        self.wormholes = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def add_wormhole(self, wormhole):
        self.wormholes.append(wormhole)

    def update(self, spaceship):
        for planet in self.planets:
            if hasattr(planet, "update"):
                planet.update()
        for wormhole in self.wormholes:
            if wormhole.check_entry(spaceship.rect):
                return wormhole.destination  # Return target system name
        return None

    def draw(self, screen):
        for planet in self.planets:
            planet.draw(screen)
        for wormhole in self.wormholes:
            wormhole.draw(screen)
