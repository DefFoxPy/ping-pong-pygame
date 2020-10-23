import pygame
import sys
import os

from .config import *
from .pelota import Pelota
from .pala import Pala

class Game:

	def __init__(self):
		pygame.init() 

		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)

		self.running = True

		self.clock = pygame.time.Clock()

		self.font = pygame.font.match_font(FONT)

		self.dir = os.path.dirname(__file__)
		self.dir_images = os.path.join(self.dir, 'sources/sprites')
	
	def start(self):
		self.new()

	def new(self):
		self.score_1 = 0
		self.score_2 = 0
		self.game_over = False
		self.fondo = pygame.image.load(os.path.join(self.dir_images, 'fondo.png'))
		self.generar_elementos()

		self.run()

	def run(self):
		while self.running:
			self.clock.tick(FPS)
			self.event()
			self.update()
			self.draw()

	def generar_elementos(self):
		self.pelota = Pelota()
		self.jugador1 = Pala(20)
		self.jugador2 = Pala(WIDTH - 20)
		self.listade_todoslos_sprites = pygame.sprite.Group()

		self.listade_todoslos_sprites.add(self.pelota)
		self.listade_todoslos_sprites.add(self.jugador1)
		self.listade_todoslos_sprites.add(self.jugador2)

	def event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_r] and self.game_over:
			self.new()

		# Movimiento del jugador 1
		if keys[pygame.K_w]:
			self.jugador1.mover_arriba()
		if keys[pygame.K_s]:
			self.jugador1.mover_abajo()

		# Movimiento del jugador 2
		if keys[pygame.K_UP]:
			self.jugador2.mover_arriba()
		if keys[pygame.K_DOWN]:
			self.jugador2.mover_abajo()

	def update(self):

		if self.game_over:
			return

		if self.pelota.rect.right < 0: # anotacion para el segundo jugador
			self.pelota.posicion_inicial()
			self.score_2 += 1

		if self.pelota.rect.left > WIDTH: # antoacion para el primer jugador
			self.pelota.posicion_inicial()
			self.score_1 += 1

		if self.score_1 == PUNTUACION_MAXIMA or self.score_2 == PUNTUACION_MAXIMA:
			self.game_over = True

		self.listade_todoslos_sprites.update()

	def draw(self):
		self.screen.blit(self.fondo, (0, 0))
		self.listade_todoslos_sprites.draw(self.screen)
		self.draw_text()
		pygame.display.flip()

	def display_text(self, text, size, color, pos_x, pos_y):
		font = pygame.font.Font(self.font, size)

		text = font.render(text, True, color)
		rect = text.get_rect()
		rect.midtop = (pos_x, pos_y)

		self.screen.blit(text, rect)

	def draw_text(self):
		self.display_text(str(self.score_1), 36, WHITE, WIDTH // 2 - 35, TEXT_POSY)
		self.display_text(str(self.score_2), 36, WHITE, WIDTH // 2 + 35, TEXT_POSY)

		if self.game_over:
			self.display_text('Juego terminado', 56, WHITE, WIDTH // 2, HEIGHT // 2)
