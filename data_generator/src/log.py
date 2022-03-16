from datetime import datetime

class Log:
	def get_timestamp() -> str:
		return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

	def error(log_text: str) -> None:
		log_string = "[Error!] " + Log.get_timestamp() + " - " + log_text + "\n"
		print(log_string)
		with open("./log.txt", "w") as file:
			file.write(log_string)
 
	def warning(log_text: str) -> None:
		log_string = "[Warning] " + Log.get_timestamp() + " - " + log_text + "\n"
		print(log_string)
		with open("./log.txt", "w") as file:
			file.write(log_string)
 
	def message(log_text: str) -> None:
		log_string = "[Message] " + Log.get_timestamp() + " - " + log_text + "\n"
		print(log_string)
		with open("./log.txt", "w") as file:
			file.write(log_string)