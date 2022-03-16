from datetime import datetime

class Time:
	def __init__(self, now: datetime) -> None:
		self.year: str = now.strftime("%Y")
		self.month: str = now.strftime("%m")
		self.day: str = now.strftime("%d")
		self.hour: str = now.strftime("%H")
		self.minute: str = now.strftime("%M")
		self.second: str = now.strftime("%S")
		self.millisecond: str = now.strftime("%f")[:-3]
 
	def __repr__(self) -> str:
		return f"{self.year}, {self.month}, {self.day}, {self.hour}, {self.minute}, {self.second}, {self.millisecond}"
 
 
class Start(Time):
	def get_headers() -> str:
		return "Start_Year, Start_Month, Start_Day, Start_Hour, Start_Min, Start_Sec, Start_MSec"
 
 
class End(Time):
	def get_headers() -> str:
		return "End_Year, End_Month, End_Day, End_Hour, End_Min, End_Sec, End_MSec"