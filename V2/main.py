import pygame
from core.game_loop import run_game
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Spaceship Game")

    clock = pygame.time.Clock()

    run_game(screen, clock)

    pygame.quit()

if __name__ == "__main__":
    main()
