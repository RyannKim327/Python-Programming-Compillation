import pygame
import random

pygame.init()


display = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Flappy Py")

speed = 15
block = 10
tube_gap = 50

color_green = (0, 200, 0)
color_blue = (0, 0, 100)

in_game = True

x = True

while in_game:

	top = display.get_height() - tube_gap
	top_tube = round(random.randrange(0, top))
	bottom_tube = top - top_tube

	if x:
		print(top_tube, bottom_tube)
		x = False

	for i in range(0, top_tube):
		pygame.draw.rect(display, color_green, [150, i, block, block])
	for i in range(bottom_tube, display.get_height()):
		pygame.draw.rect(display, color_blue, [151, i, block, block])
		
	pygame.display.update()