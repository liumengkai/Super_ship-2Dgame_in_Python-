import pygame
import game_functions as gf
class Ship():
	def __init__(self,screen):
		self.move_left=False
		self.move_right=False
		self.screen=screen
		self.images=pygame.image.load('images/littlesmall.bmp')
		self.rect=self.images.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.bottom=self.screen_rect.bottom
		self.rect.centerx=self.screen_rect.centerx
	def blitme(self):
		self.screen.blit(self.images,self.rect)
	def update(self):
		if self.move_left==True:
			self.rect.centerx-=1
		if self.move_right==True:
			self.rect.centerx+=1
			
