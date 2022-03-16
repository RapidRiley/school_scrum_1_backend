import random
from datetime import datetime

from collision import Collision

class Cyclus:
	def __init__(self, time: datetime) -> None:
		# Generate id
		self.id: str = self.get_id_string(random.randrange(0,3))
 
		self.enter_speed = random.randrange(0, 200000)
		self.exit_speed = random.randrange(80000, 300000)
 
	def get_id_string(self, id: int) -> str:
		match id:
			case 1:
				self.id = "PS"
			case 2:
				self.id = "SPS"
		return "LHC"
 
	def __repr__(self) -> str:
		return f"{self.id}, {self.enter_speed}, {self.exit_speed}"
 
	def get_headers() -> str:
		return "Cyclus_ID, Cyclus_EnterSpeed, Cyclus_ExitSpeed"
 