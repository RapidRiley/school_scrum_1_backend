from datetime import datetime
from random import randrange

from collision import Collision

class Measurement:
	def __init__(self, time: datetime):
		self.measure_point = randrange(0,8)
		self.measure_time = time.strftime("%Y%m%d%p%H%M%S")

	def __repr__(self):
		return f"{Collision.get_point_string(self.measure_point)}, {self.measure_time}"
	
	def get_headers():
		return "Measure_point, Measure_timestamp"