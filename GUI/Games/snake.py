import pygame
import random

pygame.init()

color_white = (255, 255, 255)
color_green = (0, 255, 0)
color_red = (255, 0, 0)
color_black = (0, 0, 0)
color_yellow = (0, 255, 255)
color_blue = (100, 100, 255)

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

width = 600
height = 400

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game with Google")

font_style = pygame.font.SysFont("bahnschrift", 25)
font_score = pygame.font.SysFont("comicsans", 15)

def message(msg, color,w = 3, h = 3):
	mess = font_style.render(msg, True, color)
	display.blit(mess, [display.get_width() / w, display.get_height() / h])

def your_score(score):
	value = font_score.render(f"Your score: {score}", True, color_yellow)
	display.blit(value, [0, 0])

def snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(display, color_black, [x[0], x[1], snake_block, snake_block])

def game_loop():

	last_move = -1

	snake_list = []
	length_of_snake = 1

	coordinate_x = width / 2
	coordinate_y = height / 2

	x_change = snake_block
	y_change = 0

	game_over = False
	is_close = False

	food_x = round(random.randrange(0, width - snake_block) // 10.0) * 10.0
	food_y = round(random.randrange(0, height - snake_block) // 10.0) * 10.0

	while not game_over:

		while is_close:
			display.fill(color_blue)
			message("You lose!", color_black, w = 2.5)
			message("Press Q to quit", color_black, w = 2.75, h = 2.3)
			message("Press C to continue", color_black, h = 2)
			
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						is_close = False
					if event.key == pygame.K_c:
						game_loop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and last_move != 1 and last_move != 0:
					x_change -= snake_block
					y_change = 0
					last_move = 0
				elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and last_move != 1 and last_move != 0:
					x_change = snake_block
					y_change = 0
					last_move = 1
				elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and last_move != 3 and last_move != 2:
					x_change = 0
					y_change = snake_block
					last_move = 2
				elif (event.key == pygame.K_UP or event.key == pygame.K_w) and last_move != 3 and last_move != 2:
					x_change = 0
					y_change -= snake_block
					last_move = 3
		
		if coordinate_x >= display.get_width() or coordinate_x < 0 or coordinate_y >= display.get_height() or coordinate_y < 0:
			is_close = True
		
		coordinate_x += x_change
		coordinate_y += y_change

		
		display.fill(color_white)
		pygame.draw.rect(display, color_red, [food_x, food_y, snake_block, snake_block])

		snake_head = []
		snake_head.append(coordinate_x)
		snake_head.append(coordinate_y)
		snake_list.append(snake_head)

		if len(snake_list) > length_of_snake:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x == snake_head:
				is_close = True

		snake(snake_block, snake_list)
		your_score(length_of_snake - 1)

		pygame.display.update()

		if (coordinate_x == food_x) and (coordinate_y == food_y):
			food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
			food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
			length_of_snake += 1

		clock.tick(snake_speed)

	pygame.quit()
	quit()

game_loop()