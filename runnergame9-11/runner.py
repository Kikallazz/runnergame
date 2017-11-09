import pygame
import random
import time
import math
import vector2Dfile
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

display_resolution = (display_width, display_height)
gameDisplay = pygame.display.set_mode(display_resolution)
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
fps = 120
dodge = 0

hero_img = pygame.image.load("spriteguy.png")
hero_width = 19
hero_height = 23

playerpos = vector2Dfile.Vector(0, 0);

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def obstc(x, y, width, height, colour):
    pygame.draw.rect(gameDisplay, colour, [x, y, width, height])


def car(x, y):
    gameDisplay.blit(hero_img,(x, y))


def text_object(text, font, colour):
    text_surface = font.render(text, True, colour)
    return text_surface, text_surface.get_rect()


def message_display(text, x, y, colour):
	large_text = pygame.font.Font("freesansbold.ttf",115)
	text_surf, text_rect = text_object(text, large_text,colour)
	text_rect.center = (x,y)
	gameDisplay.blit(text_surf,text_rect)
	pygame.display.update()
	time.sleep(2)

def crash(score):
	gameDisplay.fill(red)
	message_display("dEd Score = " + str(score),display_width/2,display_height/2, green)
	game()

def intro():

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					pygame.quit()
					quit()

		gameDisplay.fill(black)
		large_text = pygame.font.Font("freesansbold.ttf",115)
		text_surf, text_rect = text_object("racr 360", large_text, white)
		text_rect.center = ((display_width/2), (display_height/2))
		gameDisplay.blit(text_surf,text_rect)
		pygame.display.update()
		clock.tick(1)
		intro = False


def game():
	#GAME VARIABLES
	y = (display_height*0.8)
	x = (display_width/2)
	obstc_starty = -600
	obstc_speed = 7
	obstc_width = 50
	obstc_height = 50
	obstc_startx = random.randrange(0, display_width - obstc_width)
	x_change = 0
	y_change = 0
	dodge = 0
	# GAME LOOP
	game_end = False
	while not game_end:

		# EVENT LOOP
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
				if event.key == pygame.K_UP:
					y_change = -5
				elif event.key == pygame.K_DOWN:
					y_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
					y_change = 0



		x += x_change
		y += y_change

		# DRAW LOOP
		gameDisplay.fill(white)
		obstc(obstc_startx, obstc_starty, obstc_width, obstc_height, black)
		obstc_starty += obstc_speed
		car(x,y)
		score(dodge)

		#CRASH LOGIC
		if x >= display_width - hero_width or x <= 0:
			crash(dodge)

		if y >= display_height - hero_height or y <= 0:
			crash(dodge)

		if obstc_starty > display_height:
			obstc_starty = 0 - obstc_height
			obstc_startx = random.randrange(0, display_width)
			dodge += 1

		if y < obstc_starty + obstc_height:
			if x > obstc_startx and x < obstc_startx + obstc_width:
				crash(dodge)
			elif x + hero_width > obstc_startx and x + hero_width < obstc_startx + obstc_width:
				crash(dodge)


		#DISPLAY UPDATE
		pygame.display.update()
		clock.tick(fps)

#RUN
intro()
game()
pygame.quit()
quit()
