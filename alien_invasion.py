import sys
import pygame
from settings import Setting
from ship import Ship
def run_game():
	#初始化屏幕并且创建一个屏幕对象
	pygame.init()    #初始化
	ai_settings=Setting()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_high))        #设置屏幕大小
	bg_color=(ai_settings.screen_color)                             #设置背景颜色  
	pygame.display.set_caption("Super_ship")        #设置屏幕框显示的文字
	ship=Ship(screen)                               #将上面的screen对象传递给ship() 
	#开始游戏的主循环
	while True:                                         #每经过一次循环就刷新一下屏幕
		
		#监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:              #玩家单击quit，则pygame将侦测到pygame.Quit事件调用sys.exit()来退出
				sys.exit()
		#每次循环都会重新绘制屏幕
		screen.fill(bg_color)
		ship.blitme()
		#让最近绘制的屏幕可见
		pygame.display.flip()
run_game()
