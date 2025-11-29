import random

import pygame

from src.noisepalace.perlin_noise import PerlinNoise


def generate(
    noise_gen: PerlinNoise, size: tuple[int, int], rand: bool
) -> pygame.Surface:
    display_map = pygame.Surface(size)

    for x in range(size[0]):
        for y in range(size[1]):
            if rand:
                val = random.random()
            else:
                val = noise_gen.simple_2d(x, y)
            val = min(abs(round(val * 255)), 255)

            colour_surface = pygame.Surface((1, 1))
            colour_surface.fill((val, val, val))

            display_map.blit(colour_surface, (x, y))

    display_map = pygame.transform.scale(display_map, (350, 250))

    return display_map


def main() -> None:
    pn = PerlinNoise()
    running = True
    SCREEN_SIZE = (700, 500)

    size = (100, 100)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    display_map = generate(pn, size, False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pn = PerlinNoise()
                    display_map = generate(pn, size, False)
                elif event.key == pygame.K_s:
                    display_map = generate(pn, size, True)

        screen.blit(display_map)
        pygame.display.flip()


# def compare()


if __name__ == "__main__":
    main()
