from platform import system
import os

class ExampleData:
	def __init__(self, filename):
		self.data = ["bible", "python_code", "harry_potter_1"]

		cur_path = os.path.dirname(__file__)
		print(cur_path)

		if system == "Windows":
			path_example = "example_data\\{}.txt".format(filename)
			self.file_path = os.path.join(cur_path, path_example)

		else:
			path_example = "example_data/{}.txt".format(filename)
			self.file_path = os.path.join(cur_path, path_example)

		if filename not in self.data:
			raise FileNotFoundError("example data \"{}\" does not exist, make sure you have no typos in the name of the data!".format(filename))

	def get_raw_text(self):
		passage = ""
		with open(os.path.abspath(self.file_path), 'r') as f:
			passage = f.read().replace("\n", " ").lower()

		return passage

if __name__ == '__main__':
	print(ExampleData("bible").get_raw_text())
