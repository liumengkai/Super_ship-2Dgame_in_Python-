#coding:utf-8
class Setting():
	"""将所有关于外星人游戏的设置储存起来"""
	
	def __init__(self):                        #构造函数，不需要提供变量，必须包含self
		#屏幕设置
		self.screen_width=1500
		self.screen_height=835
		self.screen_color=(230,230,230)
		self.ship_speed_factor=1.5 
		self.bullet_speed_factor=3
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=(60,60,60)
		self.bullet_allowed=3
		self.alien_speed_factor=1
		self.fleet_direction=1                   #方向表示
		self.fleet_drop_speed=100
		self.ship_limit=3       
