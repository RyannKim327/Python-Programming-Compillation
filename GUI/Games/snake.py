import pygame
import time
import random

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption("Snake game with Google")

game_over = False

color_white = (255, 255, 255)
color_green = (0, 255, 0)
color_red = (255, 0, 0)
color_black = (0, 0, 0)

coordinate_x = 300
coordinate_y = 300

x_change = 0
y_change = 0

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
	mess = font_style.render(msg, True, color)
	display.blit(mess, [display.get_width() / 4, display.get_height() / 4])

last_move = -1

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and last_move != 1:
				x_change -= 10
				y_change = 0
				last_move = 0
			elif event.key == pygame.K_RIGHT and last_move != 0:
				x_change = 10
				y_change = 0
				last_move = 1
			elif event.key == pygame.K_DOWN and last_move != 3:
				x_change = 0
				y_change = 10
				last_move = 2
			elif event.key == pygame.K_UP and last_move != 2:
				x_change = 0
				y_change -= 10
				last_move = 3
	
	if coordinate_x >= display.get_width() or coordinate_y < 0 or coordinate_y >= display.get_height() or coordinate_y < 0:
		game_over = True

	coordinate_x += x_change
	coordinate_y += y_change
	display.fill(color_white)

	pygame.draw.rect(display, color_green, [coordinate_x, coordinate_y, 10, 10])
	pygame.display.update()
	clock.tick(30)

message("Game Over", color_black)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()