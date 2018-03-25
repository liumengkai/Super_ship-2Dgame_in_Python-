import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	"""表示单个外星人的类"""
	def __init__(self,screen):
		super().__init__()
		self.screen=screen
		self.images=pygame.image.load('images/smallalien.bmp')
		self.rect=self.images.get_rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		self.x=float(self.rect.x)
	def blitme(self,screen):
		self.screen.blit(self.images,self.rect);
