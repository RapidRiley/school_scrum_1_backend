from random import randrange
from datetime import datetime
from entry import Entry

class Batch:
	def __init__(self) -> None:
		self.creation_time = datetime.now()

		# Generate entries
		self.entries: list[Entry] = []
		for i in range(randrange(1, 1500)):
			self.entries.append(Entry())
 
	def get_file_timestamp(self) -> str:
		return self.creation_time.strftime("%Y-%h-%d_%H-%M-%S")
 
	def get_content(self) -> str:
		if len(self.entries) > 0:
			content: str = Entry.get_headers()
			for entry in self.entries:
				content += str(entry)
			return content	

		return "";
 
	def get_final_run_id(self):
		if len(self.entries) > 0:
			return self.entries[-1].run_id
		return 0;

	def get_batch_name(self) -> str:
		return f"batch_{self.get_file_timestamp()}"

	def write_file(self, output_dir: str) -> None:
		with open(f"{output_dir}/{self.get_batch_name()}.csv", "w") as file:
			file.write(self.get_content())