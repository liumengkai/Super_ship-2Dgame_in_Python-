#coding:utf-8
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,ai_settings,screen,ship):
		super(Bullet,self).__init__()
		self.screen=screen
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.bottom=ship.rect.top
		self.color=ai_settings.bullet_color
		self.y=float(self.rect.y)
		self.speed_factor=ai_settings.bullet_speed_factor
	def update(self,bullets):
		"""向上移动子弹"""
		self.y-=self.speed_factor
		self.rect.y=self.y                                  #self.rect.y表示这个rect的y坐标
		for bullet in bullets:
			if(bullet.rect.y<=0):
				bullets.remove(bullet) 
	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)         #绘制一个组的话用draw
		
