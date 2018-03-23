import pygame
import sys
import settings
def check_events(ship):
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			sys.exit()
		elif(event.type==pygame.KEYDOWN):
			if(event.key==pygame.K_RIGHT):
				##向右移动飞船
				ship.move_right=True
			if(event.key==pygame.K_LEFT):
				ship.move_left=True
		elif(event.type==pygame.KEYUP):
				if(event.key==pygame.K_RIGHT):
					ship.move_right=False
				if(event.key==pygame.K_LEFT):
					ship.move_left==False	
def update_screen(ai_settings,screen,ship):
	screen.fill(ai_settings.screen_color)          
	ship.blitme()                          #将飞船放置到正确位置
	pygame.display.flip()                  #让最近绘制的屏幕可见
