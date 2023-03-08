import pygame

pygame.init()

c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_blue = (0, 0, 255)

block = 10
movement = 5

g_width = 150
g_height = 150

display = pygame.display.set_mode((g_width, g_height))
pygame.display.set_caption("Maze game")

ingame = True

pos_x = display.get_width() // 2 - 5
pos_y = display.get_height() // 2 - 5

pygame.draw.rect(display, c_blue, [pos_x, pos_y, block, block])
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				pos_y -= movement
			elif event.key == pygame.K_DOWN:
				pos_y += movement
			elif event.key == pygame.K_LEFT:
				pos_x -= movement
			elif event.key == pygame.K_RIGHT:
				pos_x += movement
		
		display.fill(c_white)
		
		pygame.draw.rect(display, c_blue, [pos_x, pos_y, block, block])
		pygame.display.update()
