import random

class Energy: 
	def __init__(self, range_min: int, range_max: int) -> None:
		self.at_start: int = random.randrange(range_min, range_max)
		self.at_end: int = random.randrange(range_min, range_max)
 
	def __repr__(self) -> str:
		return f"{self.at_start}, {self.at_end}"
 
	def get_headers() -> str:
		return "Start_Energy, End_Energy"