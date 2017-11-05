from subprocess import call
import time

class ServoMove():
	position = 400
	def __init__(self):
		call(['gpio','mode','33','pwm'])
		self.position=400
		call(['gpio','pwm','33',str(self.position)])
	
	
	def center(self):
		self.position=400
		call(['gpio','pwm','33','300'])
		
	def accept(self):	
		self.position=500
		call(['gpio','pwm','33','500'])
		time.sleep(1.5)
		self.center()
		
	def reject(self):
		self.position=300
		call(['gpio','pwm','33','300'])
		time.sleep(1.5)
		self.center()

servo = ServoMove()
servo.accept()
