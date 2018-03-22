import pygame

class Ship():
	def __init__(self,screen):                                           #ship的构造函数，每次有一个新的对象的时候就会自动在底部中间生成一个小飞船
		"""初始化飞船，并且设置其初始位置"""
		self.screen=screen
		"""加载飞船图像并获取其外接矩形"""
		self.image=pygame.image.load('images/fly.bmp')
		self.rect=self.image.get_rect()                                 #加载出来的照片被称为suface，获取suface属性rect
		self.screen_rect=screen.get_rect()
		"""将每艘飞船放置在屏幕底端"""
		self.rect.centerx=self.screen_rect.centerx
		self.rect.left=self.screen_rect.left
	def bliteme(self):
			"""在指定位置绘制飞船"""
			self.screen.blit(self.image,self.rect)
