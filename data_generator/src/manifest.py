from datetime import datetime
import hashlib,uuid, time, json

from batch import Batch

class Manifest:
	def __init__(self, batch_list: list[str]):
		self.uuid: str = str(uuid.uuid4())
		self.creation_time: datetime = datetime.now()
		self.batch_names: list[str] = batch_list
 
	def generate_timestamp(self) -> str:
		return self.creation_time.strftime("%Y-%h-%d %H:%M:%S")

	def get_content(self) -> str:
		return {
			"uuid": self.uuid,
			"generated_on": self.generate_timestamp(),
			"batches": self.batch_names
		}

	def add_batch(self, batch_name: str):
		self.batch_names.append(batch_name)

	def write_file(self, output_dir: str):
		with open(f"{output_dir}/manifest.json", "w") as file:
			file.write(json.dumps(self.get_content()))