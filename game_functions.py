#coding:utf-8
import pygame
import sys
import settings
from bullet import Bullet
from alien import Alien
from time import sleep
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
	number_aliens_x=int(available_space_x/alien_width)          
	return number_aliens_x
def get_number_rows(ai_settings,alien_height,ship_height):
	available_space_y=ai_settings.screen_height-alien_height
	print(alien_height)
	number_rows=int((available_space_y-3*alien_height-ship_height)/alien_height)
	return number_rows
def creat_alien(ai_settings,screen,aliens,alien_number,alien_width,alien_height,number_rows):
	"""创建一个外星人并将其放在现在这行"""
	alien=Alien(ai_settings,screen)
	alien.x=alien_width+alien_width*alien_number
	alien.y=alien_height*number_rows
	alien.rect.x=alien.x                                                           #到时候绘制图像的时候是要绘制alien.rect.x和alien.rect.y的
	alien.rect.y=alien.y
	aliens.add(alien)
def check_fleet_edages(aliens,ai_settings):#如果有外星人到达了屏幕边缘直接break
	
	for alien in aliens.sprites():
		if alien.check_edges():                                  #条件满足则改变移动方向
			change_fleet_direction(ai_settings,aliens)
			break               
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,ship_height):
	"""响应被外星人装掉的飞船"""
	#将ship_left-=1
	stats.ai_settings.ship_limit-=1
	#清空外星人列表和子弹列表
	aliens.empty()
	bullets.empty()
	#创建一群新外星人，将飞船放在屏幕底部中央
	creat_fleet(ai_settings,screen,aliens,ship_height)
	ship.center_ship()
	print(stats.ai_settings.ship_limit)
	
	#暂停
	sleep(0.5)
def change_fleet_direction(ai_settings,aliens):
	for alien in aliens.sprites():                                                   #想使用alien.rect的属性必须西先遍历一遍
		alien.y+=ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,ship_height):
	screen_rect=screen.get_rect()
	for alien in aliens.sprites():
		if(alien.rect.bottom>=screen_rect.bottom):
			print('alien has come to your home losser!')
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets,ship_height)
			break
def update_aliens(ai_settings,aliens,ship,bullets,stats,screen,ship_height):                 #更新外星人的位置，如果碰到墙壁就转向
	check_fleet_edages(aliens,ai_settings)
	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,ship_height)
	aliens.update(ai_settings)                                #这个只是更新数据，没有把图片绘制在桌面上
	if(pygame.sprite.spritecollideany(ship,aliens)):         #判断外星人和飞船是否相撞
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets,ship_height)
def update_bullets(ai_settings,screen,ship,bullets,aliens,ship_height):
	bullets.update(bullets)                            #更新bullets的位置
	#删除已经消失的子弹
	for bullet in bullets.copy():
		if(bullet.rect.bottom<=0):
			bullets.remove(bullet)
	check_bullet_alien_collisions(bullets,aliens,ai_settings,screen,ship_height)
def check_bullet_alien_collisions(bullets,aliens,ai_settings,screen,ship_height):
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)   #检验碰撞函数
	if(len(aliens)==0): 
		bullets.empty()
		creat_fleet(ai_settings,screen,aliens,ship_height)
def update_screen(ai_settings,screen,ship,bullets,aliens):
	screen.fill(ai_settings.screen_color)                   
	ship.blitme()                          #将飞船放置到正确位置 
	for bullet in bullets.sprites():
		bullet.draw_bullet()                                                                               #draw_bullet()函数是让子弹显示在图像上的
	aliens.draw(screen)                     #aliens是组,不可以用Alien的函数,绘制的话需要用draw() 
	pygame.display.flip()                  #让最近绘制的屏幕可见
