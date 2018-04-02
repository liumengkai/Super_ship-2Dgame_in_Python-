#coding:utf-8
import pygame
import game_functions as gf
from settings import Setting
class Ship():
	def __init__(self,ai_setting,screen):                    #类中的函数必须是要有self的
		self.screen=screen
		self.ai_settings=Setting()
		self.images=pygame.image.load('images/small.bmp')
		self.rect=self.images.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.bottom=self.screen_rect.bottom
		self.rect.centerx=self.screen_rect.centerx
		self.center=float(self.rect.centerx)                 ##因为rect的centerx只能存储整数所以需要在飞船的center属性中存储小数
		self.move_left=False
		self.move_right=False
		#在正确位置画出飞船
	def blitme(self):
		self.screen.blit(self.images,self.rect)
		#更新屏幕
	def update(self):
		if self.move_left and self.rect.left>self.screen_rect.left:
			self.center-=self.ai_settings.ship_speed_factor
		if self.move_right and self.rect.right<self.screen_rect.right:
			self.center+=self.ai_settings.ship_speed_factor
		self.rect.centerx=self.center
