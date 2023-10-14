import pygame

pygame.init()

c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_blue = (0, 0, 255)
c_green = (0, 150, 0)
c_red = (100, 0, 0)

block = 25
movement = 25

g_width = 500
g_height = 500

display = pygame.display.set_mode((g_width, g_height))
pygame.display.set_caption("Maze game")

ingame = True

base_x = 225
base_y = 225

pos_x = base_x # display.get_width() // 2 - 5
pos_y = base_y # display.get_height() // 2 - 5

'''pattern = [
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
	
]'''

'''
  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
1     *           * * *                 *
2 *       * * *         * *   * * * * * *
3 * * * * * * * * * *   * *             *
4 * *                   * *   * * * *   *
5 * *   * * * * * * * *   *   * *       *
6 * *   *                 *   * *   * * *
7 *     *   * * * * * * * *   * *   * * *
8 *   *     *             *   * *       *
9 *   *   * *   * * * *   *   * * * *   *
0 *   *   * *   * * * *   *       * *   *
1 *   *         *   * *   * * *   * *   *
2 *       * * * *   * *           * *   *
3 * * * *           * * * * * * *   *   *
4 *         * * * * * * * * * * *   *   *
5 *   * *   * *                 *   *   *
6 * * * *   * *   * * * * * *   *   *   *
7 *         * *   *             *   *   *
8 *   * * * * *   *   * * * * * *   *   *
9 *               *                     *
0 * * * * * * * * * * * * * * * * * * * *
  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
'''

pattern = []
xs = [
	[1, 2, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19],
	[2, 3, 4, 8, 9, 10, 11, 14],
	[11, 14, 15, 16, 17, 18, 19],
	[3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 19],
	[3, 12, 14, 17, 18, 19],
	[3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 17],
	[2, 3, 5, 14, 17],
	[2, 4, 5, 7, 8, 9, 10, 11, 12, 14, 17, 18, 19],
	[2, 4, 7, 12, 14, 19],
	[2, 4, 7, 9, 10, 12, 14, 15, 16, 19],
	[2, 4, 5, 6, 7, 9, 12, 16, 19],
	[2, 3, 4, 9, 12, 13, 14, 15, 16, 19],
	[5, 6, 7, 8, 9, 17, 19],
	[2, 3, 4, 5, 17, 19],
	[2, 5, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19],
	[5, 8, 15, 17, 19],
	[2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 15, 17, 19],
	[2, 8, 10, 17, 19],
	[2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
]

target = [0, 0]

for y in range(len(xs)):
	for x in range(len(xs[y])):
		pattern.append([(int(xs[y][x]) - 1) * block, y * block])

font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color = c_green, w = 3, h = 3):
	# Mesasge or text in the game
	mess = font_style.render(msg, True, color)
	display.blit(mess, [display.get_width() / w, display.get_height() / h])

pygame.draw.rect(display, c_blue, [pos_x, pos_y, block, block])

gaming = True
while gaming:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gaming = False
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

		pygame.draw.rect(display, c_green, [target[0], target[1], block, block])
		pygame.draw.rect(display, c_red, [base_x, base_y, block, block])
		
		if pos_x == target[0] and pos_y == target[1]:
			message("Congrats")

		if pos_x == base_x and pos_y == base_y:
			message("Start now")
		
		pygame.draw.rect(display, c_blue, [pos_x, pos_y, block, block])
		pygame.display.update()
