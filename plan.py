'''
position 
get key
if keydown "left arrow"
    move position left 

if keydown "right arrow"
    move position right

'''
import pygame

#screen display
pygame.init()
WIDTH, HEIGHT, = 640, 480
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing")

clock = pygame.time.Clock()

#colors
BLACK = (0, 0, 0)

screen.fill(BLACK)

#create sprite
player_rect = pygame.Rect(WIDTH // 2, HEIGHT // 1, 30, 30)
coin_circl = pygame.Circle(WIDTH // 2, HEIGHT // 5, 10, 10)
