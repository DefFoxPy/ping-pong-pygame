import pygame
import math

from .config import *


def es_positivo(valor):
	return abs(valor) == valor

class Pelota(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([ball_width, ball_height])
		self.image.fill(WHITE)

		self.rect = self.image.get_rect()
		
		self.speed_x = ball_speed
		self.speed_y = ball_speed

		self.posicion_inicial()

	def posicion_inicial(self):
		self.rect.center = (WIDTH // 2, HEIGHT // 2)
		self.speed_y = 0
		self.speed_x = self.speed_x * 0.5 

	def update(self):

		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

		if self.rect.top < 0 or self.rect.bottom > HEIGHT:
			self.speed_y *= -1

		if self.rect.right < 0 or  self.rect.left > WIDTH:
			self.speed_x *= -1

	def hay_colision(self, paleta):
		# Verificamos si en verdad hay una colision entre la pelota y un jugador
		if pygame.sprite.collide_rect(self, paleta):

			distancia = abs(paleta.rect.centery - self.rect.centery)
			if self.rect.centery >= paleta.rect.centery:
				self.speed_y = 2 * ball_speed * math.sin(math.radians(distancia))
			else:
				self.speed_y = 2 * ball_speed * -math.sin(math.radians(distancia))
			
			if es_positivo(self.speed_x): # positivo
				self.rect.right = paleta.rect.left
			else: # negativo
				self.rect.left = paleta.rect.right

			self.speed_x *= -1.1

			print('Velocidad de la pelota')
			print('x={} \n y={}'.format(self.speed_x, self.speed_y))
			print('distancia=', distancia)


	def stop(self):
		self.speed_x = 0
		self.speed_y = 0 
