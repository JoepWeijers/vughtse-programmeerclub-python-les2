import sys, pygame
from tkinter import *

pygame.init()

width = 1550
height = 880
speed = [1, 1]
black = 0, 0, 0

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

screen = pygame.display.set_mode((width, height))
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: running = False
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()