import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	"""表示单个外星人的类"""
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		self.image=pygame.image.load('images/smallalien.bmp')           #在这里传入图形的时候必须叫做image，不可以叫做其他的名字否则不可以用pygame中的draw等自带函数
		self.rect=self.image.get_rect()                                 #将图像返回成rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		self.x=float(self.rect.x)
	#def blitme(self):
		#self.screen.blit(self.image,self.rect);
	def check_edges(self,screen):
		screen_rect=self.screen.get_rect()
		if(self.rect.right>=screen_rect.right):
			return True
		elif self.rect.left<=0:
			 return True
	def update(self,ai_settings):
		self.x+=(ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)                   #self.rect.x是只能存储实数的变量
		self.rect.x=self.x
		
