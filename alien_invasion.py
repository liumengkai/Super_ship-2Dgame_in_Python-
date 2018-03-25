import sys
import pygame
from ship import Ship
from settings import Setting
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
def run_game():
	#初始化屏幕并且创建一个屏幕对象
	pygame.init()    #初始化
	ai_settings=Setting()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_high))        #创建了一个屏幕对象screen设置屏幕大小
	bg_color=(ai_settings.screen_color)                             #设置背景颜色  
	pygame.display.set_caption("Super_ship")        #设置屏幕框显示的文字
	ship = Ship(ai_settings,screen)                              #创建一艘飞船，不可以放在while循环中
	bullets=Group()
	alien = Alien(screen)
	#开始游戏的主循环
	while True:                                         #每经过一次循环就刷新一下屏幕
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_screen(ai_settings,screen,ship,bullets,alien)                #每次循环都会重新绘制屏幕 #必须先进行填充背景色#将飞船放置在底端中间#让最近绘制的屏幕可见		                         		
run_game()
