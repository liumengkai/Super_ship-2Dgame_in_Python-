import pygame
import sys
import settings
from bullet import Bullet
from alien import Alien
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
		else:
			return
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
def creat_fleet(ai_settings,screen,aliens,ship_height):                                       #创建一群外星人
	 """创建外星人群，并计算每行可容纳多少个外星人"""
	 alien=Alien(ai_settings,screen)
	 alien_width=alien.rect.width
	 alien_height=alien.rect.height
	 number_alien_x=get_number_aliens_x(ai_settings,alien_width)
	 number_rows_y=get_number_rows(ai_settings,alien_height,ship_height)
	 for alien_number in range(number_alien_x):
		 for alien_rows in range(number_rows_y):
			 creat_alien(ai_settings,screen,aliens,alien_number,alien_width,alien_height,alien_rows )
def get_number_aliens_x(ai_settings,alien_width):                          #获得一行外星人有多少
	available_space_x=ai_settings.screen_width-2*alien_width
	print(available_space_x)
	number_aliens_x=int(available_space_x/alien_width)          
	return number_aliens_x
def get_number_rows(ai_settings,alien_height,ship_height):
	available_space_y=ai_settings.screen_height-alien_height
	number_rows=int((available_space_y-3*alien_height-ship_height)/alien_height)
	return number_rows
def creat_alien(ai_settings,screen,aliens,alien_number,alien_width,alien_height,number_rows):
	"""创建一个外星人并将其放在现在这行"""
	alien=Alien(ai_settings,screen)
	alien.x=alien_width*alien_number
	alien.y=alien_height*number_rows
	alien.rect.x=alien.x                                                           #到时候绘制图像的时候是要绘制alien.rect.x和alien.rect.y的
	alien.rect.y=alien.y
	aliens.add(alien)
def check_fleet_edages(aliens,screen,ai_settings):
	for alien in aliens :
		if alien.check_edges(screen):
			change_fleet_direction(ai_settings,aliens)
			break                                                        #如果有外星人到达了屏幕边缘直接break
def change_fleet_direction(ai_settings,aliens):
	for alien in aliens:                                                   #想使用alien.rect的属性必须西先遍历一遍
		alien.rect.y-=ai_settings.fleet_drop_speed
		ai_settings.fleet_direction*= -1
def update_aliens(ai_settings,aliens,screen):
	check_fleet_edages(aliens,screen,ai_settings)
	aliens.update(ai_settings)
def update_screen(ai_settings,screen,ship,bullets,aliens):
	screen.fill(ai_settings.screen_color)          
	for bullet in bullets.sprites():                          #函数sprites返回了一个列表，其中包含编组bullets中的所有精灵
		bullet.draw_bullet()                               #遍历组中的每个元素并且对其调用draw_bullet()函数
		bullet.update(bullets)                                   
	ship.blitme()                          #将飞船放置到正确位置
	aliens.draw(screen)                     #aliens是组,不可以用Alien的函数,绘制的话需要用draw() 
	pygame.display.flip()                  #让最近绘制的屏幕可见
