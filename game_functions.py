import pygame
import sys
import settings
from bullet import Bullet
def check_keydown_event(event,ai_settings,screen,ship,bullets):                          #因为没有函数for event in pygame.event.get()需要添加形参event来表示event的含义
	if(event.key==pygame.K_RIGHT):                                                       #检查按键事件函数
		ship.move_right=True
	elif(event.key==pygame.K_LEFT):
		ship.move_left=True
	elif(event.key==pygame.K_SPACE):
		fire_bullet(event,ai_settings,bullets,screen,ship) 
	elif(event.key==pygame.K_q):
		sys.exit()                                      
def fire_bullet(event,ai_settings,bullets,screen,ship):                                     #点击空格开火函数
		if(len(bullets)<=ai_settings.bullet_allowed):
			new_bullet=Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)
		else:return
def check_keyup_event(event,ship):                                            #检查抬起按键的函数
	if(event.key==pygame.K_RIGHT):
		ship.move_right=False
	if(event.key==pygame.K_LEFT):
		ship.move_left=False
def check_events(ai_settings,screen,ship,bullets):                         #检查所有事件的总函数
	for event in pygame.event.get():                                       #必须先确定event是什么事件类型才可以进行下一步，确定event是event.KETDOWN然后确定是什么键
		if(event.type==pygame.KEYDOWN):
			check_keydown_event(event,ai_settings,screen,ship,bullets)                   #调用上面的函数时候需要给出形参event，这里有函数for...所以可以直接当作已知
		elif(event.type==pygame.KEYUP):
			check_keyup_event(event,ship)	
def update_screen(ai_settings,screen,ship,bullets,alien):
	screen.fill(ai_settings.screen_color)          
	for bullet in bullets.sprites():                          #函数sprites返回了一个列表，其中包含编组bullets中的所有精灵
		bullet.draw_bullet()                               #遍历组中的每个元素并且对其调用draw_bullet()函数
		bullet.update(bullets)                                  
	alien.blitme(screen)
	ship.blitme()                          #将飞船放置到正确位置
	pygame.display.flip()                  #让最近绘制的屏幕可见
