import hashlib
  
# encoding GeeksforGeeks using md5 hash
# function 

class Hash:
	def __init__(self, content: str) -> None:
		self.hash = hashlib.md5(content.encode())

	def get_hash(self) -> str:
		return self.hash.hexdigest()
	
	def write_file(self, output_dir: str, file_name: str):
		with open(f"{output_dir}/{file_name}.md5", "w") as file:
			file.write(self.get_hash())
