import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1300, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Solar System")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # Sun
GRAY = (169, 169, 169)  # Mercury
LIGHT_GRAY = (192, 192, 192)  # Venus
DODGER_BLUE = (30, 144, 255)  # Earth
TOMATO = (255, 99, 71)  # Mars
GOLD = (255, 165, 0)  # Jupiter
LIGHT_SKY_BLUE = (135, 206, 250)  # Saturn
STEEL_BLUE = (70, 130, 180)  # Uranus
MIDNIGHT_BLUE = (25, 25, 112)  # Neptune

# Planet data: (color, radius, distance from sun, speed)
planets = [
    (YELLOW, 20, 0, 0),  # Sun
    (GRAY, 5, 50, 4),  # Mercury
    (LIGHT_GRAY, 8, 90, 3.5),  # Venus
    (DODGER_BLUE, 10, 140, 2.5),  # Earth
    (TOMATO, 7, 190, 2),  # Mars
    (GOLD, 25, 300, 1.8),  # Jupiter
    (LIGHT_SKY_BLUE, 22, 450, 1.4),  # Saturn
    (STEEL_BLUE, 19, 600, 1.2),  # Uranus
    (MIDNIGHT_BLUE, 18, 750, 1),  # Neptune
]

# Game loop
running = True
angle = 0
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Draw sun at center
    pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 2), 20)

    # Draw planets
    for color, radius, distance, speed in planets[1:]:
        x = WIDTH // 2 + int(distance * math.cos(math.radians(angle * speed)))
        y = HEIGHT // 2 + int(distance * math.sin(math.radians(angle * speed)))
        pygame.draw.circle(screen, color, (x, y), radius)

    # Update display
    pygame.display.flip()
    angle += 1
    clock.tick(60)  # Limit to 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
