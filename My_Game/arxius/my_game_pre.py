#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import pygame
import random
from pygame.locals import *
 
# Constantes
WIDTH = 900
HEIGHT = 600
 
# --------------------------------------------------------------------- 
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
		if self.rect.top >= 60:
			if keys[K_UP]:
				self.rect.centery -= self.speed * time
		if self.rect.bottom <= HEIGHT:
			if keys[K_DOWN]:
				self.rect.centery += self.speed * time

class met(pygame.sprite.Sprite):
	def __init__(self, x):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("images/meteorito.png", True)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = HEIGHT / 2
		self.speed = 0.5
	def reset_pos(self):
		self.rect.y = random.randrange(60, 550, 60)
		self.rect.x = 850
        
	def actualizar(self, time, nave_pri,vel):
		self.rect.x += vel
		if self.rect.x < 0:
			self.reset_pos()
		if pygame.sprite.collide_rect(self, nave_pri):
			self.reset_pos()
class disparo(pygame.sprite.Sprite):
	def __init__(self, nave_pri):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("images/disparo.png", True)
		self.rect = self.image.get_rect()
		self.rect.centerx = 900
		self.rect.centery = -5
		self.speed = 0.5
	def actualizar(self, time, nave_pri,keys, disp,mets,puntu):
		self.rect.x += 8
		if disp.rect.centerx >= 900:
			if keys[K_SPACE]:
				self.rect.y = nave_pri.rect.centery
				self.rect.x = 70
		if pygame.sprite.collide_rect(self, mets):
			self.rect.x = 900
			mets.reset_pos()
			puntu[0] += 10

# ---------------------------------------------------------------------
# Funciones generales
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
def texto(texto, posx, posy, color=(255, 255, 255)):
	fuente = pygame.font.Font("Varios/another/coalition.ttf", 25)
	salida = pygame.font.Font.render(fuente, texto, 1, color)
	salida_rect = salida.get_rect()
	salida_rect.centerx = posx
	salida_rect.centery = posy
	return salida, salida_rect
# ---------------------------------------------------------------------
# Funciones del juego
# ---------------------------------------------------------------------
def velo(num):
    if num > -10:
        num= num-0.001
    else:
        num= num- 0.0005
    return num
# ---------------------------------------------------------------------
# Programa Principal
# --------------------------------------------------------------------- 
def main():
# Inicializaciones pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Invaders")
    background_image = load_image('images/fondo-triangle.jpg')

# Inicializaciones elementos de juego
    nave_pri = nave(55)
    disp = disparo(nave_pri)
    mete = met(850)
    mete1 = met(1450)
    mete2 = met(1850)
    mete3 = met(2250)
    vel = -5
    puntu = [0]
    clock = pygame.time.Clock()
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        vel = velo(vel)
# Procesamos ia
        mete.actualizar(time,nave_pri,vel)
        mete1.actualizar(time,nave_pri,vel)
        mete2.actualizar(time,nave_pri,vel)
        mete3.actualizar(time,nave_pri,vel)
        disp.actualizar(time,nave_pri,keys,disp,mete,puntu)
        disp.actualizar(time,nave_pri,keys,disp,mete1,puntu)
        disp.actualizar(time,nave_pri,keys,disp,mete2,puntu)
        disp.actualizar(time,nave_pri,keys,disp,mete3,puntu)
        
# Procesamos jugador
        nave_pri.mover(time, keys)
# Otros
        p_jug, p_jug_rect = texto(str(puntu[0]), 500, 40)
# Actualizamos estado de la partida
        screen.blit(background_image, (0, 0))
        screen.blit(p_jug, p_jug_rect)
        screen.blit(disp.image, disp.rect)
        screen.blit(mete.image, mete.rect)
        screen.blit(mete1.image, mete1.rect)
        screen.blit(mete2.image, mete2.rect)
        screen.blit(mete3.image, mete3.rect)
        screen.blit(nave_pri.image, nave_pri.rect)
# Renderizamos
        
        pygame.display.flip()


    return 0
if __name__ == '__main__':
    pygame.init()
    main()
