import pygame

from .config import *

class Pala(pygame.sprite.Sprite):

	def __init__(self, pos_x):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([pala_width, pala_height])
		self.image.fill(WHITE)

		self.rect = self.image.get_rect()
		self.rect.centerx = pos_x
		self.rect.centery = pala_pos_y

		self.speed = pala_speed

	def mover_arriba(self):
		self.rect.y -= self.speed

	def mover_abajo(self):
		self.rect.y += self.speed

	def update(self):
		if self.rect.top < 0:
			self.rect.top = 0

		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
