#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import pygame
from pygame.locals import *
 
# Constantes
WIDTH = 900
HEIGHT = 600
 
# Clases
# ---------------------------------------------------------------------
class nave(pygame.sprite.Sprite):
	def __init__(self, x):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("images/nave.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = HEIGHT / 2
		self.speed = 0.5
	def mover(self, time, keys):
		if self.rect.top >= 0:
			if keys[K_UP]:
				self.rect.centery -= self.speed * time
		if self.rect.bottom <= HEIGHT:
			if keys[K_DOWN]:
				self.rect.centery += self.speed * time
class disparo(pygame.sprite.Sprite):
	def__init__(self,posx,posy):
		pygame.sprite.Sprite.__init__(self)
		self.imagedisparo = pygame.image.load('images/disparo.png')	
		self.rect = self.imagedisparo.get_rect()
		self.velocidadDisparo = 5
		self.rect.top = posy
		self.rect.left = posx
	def trayectoria(self):
		self.rect.x += 5

# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
	try: image = pygame.image.load(filename)
	except pygame.error, message:
		raise SystemExit, message
	#image = image.convert()
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color, RLEACCEL)
	return image 
# ---------------------------------------------------------------------
 
def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Invaders")
	background_image = load_image('images/fondo-triangle.jpg')
	nave_pri = nave(55)
	clock = pygame.time.Clock()

	while True:
		time = clock.tick(60)
		keys = pygame.key.get_pressed()
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
		nave_pri.mover(time, keys)
		screen.blit(background_image, (0, 0))
		screen.blit(nave_pri.image, nave_pri.rect)
		pygame.display.flip()

	return 0
if __name__ == '__main__':
	pygame.init()
	main()