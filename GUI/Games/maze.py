import pygame

pygame.init()

c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_blue = (0, 0, 255)
c_green = (0, 150, 0)

block = 10
movement = 10

g_width = 200
g_height = 200

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

font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color = c_green, w = 3, h = 3):
	# Mesasge or text in the game
	mess = font_style.render(msg, True, color)
	display.blit(mess, [display.get_width() / w, display.get_height() / h])

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
		
		if pos_x == pattern[len(pattern) - 1][0] and pos_y == pattern[len(pattern) - 1][1]:
			message("Congrats")
		
		pygame.draw.rect(display, c_blue, [pos_x, pos_y, block, block])
		pygame.display.update()
