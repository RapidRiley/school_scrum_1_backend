from random import randrange

class Run_ID:
	def __init__(self):
		self.id: str = ""
		for i in range(0, 8):
			self.id += str(0) if randrange(0,2) == 1 else str(1)

	def __repr__(self):
		return f"{self.id}"

	def get_headers():
		return "Run_ID"
