import pygame

from .config import *

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

	def update(self):

		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

		if self.rect.top < 0 or self.rect.bottom > HEIGHT:
			self.speed_y *= -1

		if self.rect.right < 0 or  self.rect.left > WIDTH:
			self.speed_x *= -1


	def stop(self):
		self.speed_x = 0
		self.speed_y = 0
