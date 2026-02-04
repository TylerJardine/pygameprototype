import pygame
import sys

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Money Grab Game Jam")

clock = pygame.time.Clock()

# Colors
WHITE = (150, 255, 255)
GRAY = (100, 100, 100)

# Floor (background rectangle)
floor_height = 100
floor_rect = pygame.Rect(
    0,
    HEIGHT - floor_height,
    WIDTH,
    floor_height
)

# Player settings
player_width, player_height = 40, 60
player_x = WIDTH // 2 - player_width // 2
player_y = floor_rect.top - player_height
player_speed = 5

player_rect = pygame.Rect(
    player_x,
    player_y,
    player_width,
    player_height
)

# Game loop
running = True
while running:
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # Keep player on screen
    player_rect.x = max(0, min(player_rect.x, WIDTH - player_width))

    # Drawing
    screen.fill(WHITE)

    # Draw floor
    pygame.draw.rect(screen, GRAY, floor_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()