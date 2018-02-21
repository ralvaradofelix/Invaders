#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
"""
 
import pygame
import random
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
 
# Esta clase representa la pelota.     
# Deriva de la clase "Sprite" en Pygame.
class Bloque(pygame.sprite.Sprite):
     
    # Constructor. Pasa el color del bloque, 
    # así como su posición x,y
    def __init__(self, color, largo, alto):
        # Llamada al constructor de la clase padre (Sprite) 
        super().__init__() 
 
        # Creamos una imagen del bloque y la rellenamos de color.
        # También se podría emplear una imagen guardada en disco.
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
 
        # Extraemos el objeto rectángulo que posee las dimensiones de la imagen.
        # Estableciendo los valores rect.x e rect.y, actualizamos la posición de este objeto.
        self.rect = self.image.get_rect()
 
# Inicializamos Pygame
pygame.init()
 
#  Establecemos el alto y largo de la pantalla
LARGO_PANTALLA = 700
ALTO_PANTALLA = 400
pantalla=pygame.display.set_mode([LARGO_PANTALLA, ALTO_PANTALLA])
 
# Esta es una lista con los 'sprites.'Cada bloque en el programa es
# añadido a la lista. La lista es gestionada por la clase llamada 'Group.'
listade_bloques = pygame.sprite.Group()
 
# Esta es una lista de cada sprite. En ella están todos los bloques, incluido el del protagonista.
listade_todolos_sprites = pygame.sprite.Group()
 
for i in range(10):
    # Esto representa un bloque
    bloque = Bloque(NEGRO, 20, 15)
 
    # Establecemos una ubicación aleatoria para el bloque.
    bloque.rect.x = random.randrange(LARGO_PANTALLA)
    bloque.rect.y = random.randrange(ALTO_PANTALLA)
     
    # Añadimos el bloque a la lista de objetos.
    listade_bloques.add(bloque)
    listade_todolos_sprites.add(bloque)
 
#Creamos un bloque protagonista ROJO
protagonista = Bloque(ROJO, 20, 15)
listade_todolos_sprites.add(protagonista)
 
# Iteramos hasta que el usuario haga click sobre el botón de salir.
hecho = False
 
#Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
# Esta es la fuente que usaremos para dibujar el texto en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
 
# Puntuación actual
puntuacion = 0
 
# Nivel actual
nivel = 1
 
# -------- Bucle principal del Programa -----------
while not hecho:
    #TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
     
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Anuncio que hemos terminado por lo que abandonamos el bucle
 
    # Obtenemos la posición actual del ratón. Nos la devuelve como
    # una lista de dos números.
    pos = pygame.mouse.get_pos()
     
    #TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
     
    # Extraemos de la lista los valores de x e y, 
    # tal como si extrajéramos letras de una cadena de texto.
    # Situamos al objeto protagonista en la ubicación del ratón.
    protagonista.rect.x = pos[0]
    protagonista.rect.y = pos[1]
     
    #  Observamos por si el bloque protagonista ha colisionado contra algo.
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, listade_bloques, True)  
     
    # Comprobamos la lista de colisiones
    for bloque in lista_impactos_bloques:
        puntuacion += 1
        print( puntuacion )
 
    # Comprobamos si todos los bloques han desparecido.
    # Si es así, subimos un nivel.
    if len(listade_bloques) == 0:
        # Sumamos 1 al nivel.
        nivel += 1
 
        # Añadimos más bloques. El número dependerá del nivel.
        # Podríamos, también usar una declaración 'if' para singularizar qué sucede
        # en los niveles 2, 3, 4, etc.
        for i in range(nivel * 10):
            # Esto representa un bloque
            bloque = Bloque(NEGRO, 20, 15)
 
            # Establecemos una ubicación aleatoria para el bloque.
            bloque.rect.x = random.randrange(LARGO_PANTALLA)
            bloque.rect.y = random.randrange(ALTO_PANTALLA)
             
            # Añadimos el bloque a la lista de objetos.
            listade_bloques.add(bloque)
            listade_todolos_sprites.add(bloque)
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO 
 
    # Limpiamos la pantalla
    pantalla.fill(BLANCO)
 
    # Dibujamos todos los sprites
    listade_todolos_sprites.draw(pantalla)
     
    texto = fuente.render("Puntuación: " + str(puntuacion), True, NEGRO)
    pantalla.blit(texto, [10, 10])
         
    texto = fuente.render("Nivel: " + str(nivel), True, NEGRO)
    pantalla.blit(texto, [10, 40])
     
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
     
    # Limitamos a 60 fps
    reloj.tick(60)
 
    # Avanzamos y actualizamos la pantalla que ya hemos dibujado.
    pygame.display.flip()
 
pygame.quit()