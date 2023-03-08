import pygame

pygame.init()

c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_blue = (0, 0, 255)

block = 10
movement = 10

g_width = 150
g_height = 150

display = pygame.display.set_mode((g_width, g_height))
pygame.display.set_caption("Maze game")

ingame = True

pos_x = display.get_width() // 2 - 5
pos_y = display.get_height() // 2 - 5

pattern = [
	[pos_x, pos_y],
	[pos_x + 10, pos_y],
	[pos_x + 10, pos_y + 10],
	[pos_x + 10, pos_y + 20],
	[pos_x, pos_y + 20],
	[pos_x, pos_y + 30],
	[pos_x, pos_y + 40],
	[pos_x + 10, pos_y + 40],
	[pos_x + 20, pos_y + 40],
	[pos_x + 30, pos_y + 40],
	[pos_x + 30, pos_y + 30],
	[pos_x + 30, pos_y + 20],
	[pos_x + 30, pos_y + 10],
	[pos_x + 30, pos_y],
	[pos_x + 30, pos_y - 10],
	[pos_x + 30, pos_y - 20],
	[pos_x + 30, pos_y - 30],
	[pos_x + 30, pos_y - 40],
	[pos_x + 20, pos_y - 40],
	[pos_x + 10, pos_y - 40],
	[pos_x + 10, pos_y - 30],
	[pos_x + 10, pos_y - 20],
	[pos_x, pos_y - 20],
	[pos_x - 10, pos_y - 20],
	[pos_x - 20, pos_y - 20],
	[pos_x - 30, pos_y - 20],
	[pos_x - 30, pos_y - 10],
	[pos_x - 30, pos_y],
	[pos_x - 20, pos_y],
	[pos_x - 20, pos_y + 10],
	[pos_x - 20, pos_y + 20],
	[pos_x - 20, pos_y + 30],
	[pos_x - 20, pos_y + 40],
	[pos_x - 20, pos_y + 50],
	[pos_x - 30, pos_y + 50],
	[pos_x - 40, pos_y + 50],
	[pos_x - 50, pos_y + 50],
	[pos_x - 50, pos_y + 40],
	[pos_x - 50, pos_y + 30],
	[pos_x - 50, pos_y + 20],
	[pos_x - 50, pos_y + 10],
	[pos_x - 50, pos_y],
	[pos_x - 50, pos_y - 10],
	[pos_x - 50, pos_y - 20],
	[pos_x - 50, pos_y - 30],
	[pos_x - 50, pos_y - 40],
	[pos_x - 50, pos_y - 50],
	[pos_x - 40, pos_y - 50],
	[pos_x - 30, pos_y - 50],
	[pos_x - 20, pos_y - 50],
	[pos_x - 10, pos_y - 50],
	[pos_x, pos_y - 50],
	[pos_x, pos_y - 60],
	[pos_x, pos_y - 70],
	[pos_x - 10, pos_y - 70],
	[pos_x - 20, pos_y - 70],
	[pos_x - 30, pos_y - 70],
	[pos_x - 40, pos_y - 70],
	[pos_x - 50, pos_y - 70],
	[pos_x - 60, pos_y - 70],
	[pos_x - 70, pos_y - 70]
	
]

pygame.draw.rect(display, c_blue, [pos_x, pos_y, block, block])
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				pos_y -= movement
				if not [pos_x, pos_y] in pattern:
					pos_y += movement
			elif event.key == pygame.K_DOWN:
				pos_y += movement
				if not [pos_x, pos_y] in pattern:
					pos_y -= movement
			elif event.key == pygame.K_LEFT:
				pos_x -= movement
				if not [pos_x, pos_y] in pattern:
					pos_x += movement
			elif event.key == pygame.K_RIGHT:
				pos_x += movement
				if not [pos_x, pos_y] in pattern:
					pos_x -= movement
		
		display.fill(c_black)
		
		for i in pattern:
			pygame.draw.rect(display, c_white, [i[0], i[1], block, block])
		
		pygame.draw.rect(display, c_blue, [pos_x, pos_y, block, block])
		pygame.display.update()
