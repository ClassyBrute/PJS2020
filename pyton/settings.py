import pygame
pygame.font.init()

# setting screen dimensions
screen_width = 1200
screen_height = 600

# defining basic colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 180)
light_blue = (40, 80, 250)

# basic frames per second
fps = 30

# time counting
clock = pygame.time.Clock()

# setting up the display
screen = pygame.display.set_mode((screen_width, screen_height))

# defining fonts
smallfont = pygame.font.SysFont("suruma", 25)
medfont = pygame.font.SysFont("surma", 50)
largefont = pygame.font.SysFont("surma", 80)
