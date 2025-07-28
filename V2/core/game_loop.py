import pygame
from config import DARK_SPACE, FPS
from entities.spaceship import Spaceship
from entities.planet import Planet
from entities.wormhole import Wormhole
from systems.solar_system import SolarSystem
from systems.galaxy_map import GalaxyMap

def run_game(screen, clock):
    # Initialize game objects

    # Create gamespace
    galaxy = GalaxyMap()
    galaxy.load_from_folder("assets/data/world/sector/starssystem")

    # Create first solar system




    spaceship = Spaceship(x=100, y=100)

    running = True
    while running:
        clock.tick(FPS)

        # --- Handle Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        spaceship.handle_input(keys)

        # --- Update Game State ---
        spaceship.update()
        next_system = galaxy.current_system.update(spaceship)
        if next_system:
            galaxy.switch_system(next_system)

        # --- Draw Everything ---
        screen.fill(DARK_SPACE)
        spaceship.draw(screen)
        galaxy.draw(screen)
        pygame.display.flip()
