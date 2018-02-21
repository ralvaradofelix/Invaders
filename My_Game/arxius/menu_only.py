import pygame

class cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self,0,0,1,1)
	def update(self):
		self.left,self.top=pygame.mouse.get_pos()

class boton(pygame.sprite.Sprite):
	def __init__(self,imagen1,imagen2,x=200,y=200):
		self.imagen_normal=imagen1
		self.imagen_seleccion=imagen2
		self.imagen_actual=self.imagen_normal
		self.rect=self.imagen_actual.get_rect()
		self.rect.left,self.rect.top=(x,y)
	def update(self,pantalla,cursor):
		if cursor.colliderect(self.rect):
			self.imagen_actual=self.imagen_seleccion
		else:
			self.imagen_actual=self.imagen_normal
		pantalla.blit(self.imagen_actual,self.rect)
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

def main():
	pygame.init()

	screen=pygame.display.set_mode((900,600))

	pygame.display.set_caption("Invaders")

	reloj1=pygame.time.Clock()

	ini_game=pygame.image.load("images/menu/ij.png")
	ini_game_os=pygame.image.load("images/menu/ij_os.png")
	como_jugar=pygame.image.load("images/menu/cj.png")
	como_jugar_os=pygame.image.load("images/menu/cj_os.png")
	salir_g=pygame.image.load("images/menu/s_nos.png")
	salir_g_os=pygame.image.load("images/menu/s.png")
	op1=boton(ini_game,ini_game_os,340,210)
	op2=boton(como_jugar,como_jugar_os,350,250)
	op3=boton(salir_g,salir_g_os,390,290)
	cursor1=cursor()
	salir=False
	background_image = load_image('images/fondo-triangle.jpg')
	logo = load_image('images/logo.png')

	while salir!=True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=True
		reloj1.tick(20)
		cursor1.update()
		screen.blit(background_image, (0, 0))
		screen.blit(logo, (180, 80))
		op1.update(screen,cursor1)
		op2.update(screen,cursor1)
		op3.update(screen,cursor1)
		pygame.display.update()
	pygame.quit()
main()