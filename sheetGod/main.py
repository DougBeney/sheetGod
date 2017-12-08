import sys
import pyexcel

from .commands import Commands


class sheetGod():
	theFile = None
	theSheet = None
	isLoaded = False
	test1 = "itWorked"

	def loadSheet(self, file_name=None):
		if not file_name:
			file_name = input("Enter a filename: ")

		try:
			sheet = pyexcel.get_sheet(file_name=file_name)
		except:
			print("Can't read file [%s]..." % file_name)
			return self.loadSheet()
		else:
			return sheet

	def cleanse_func(self, v):
		v = str(v)
		v = v.replace("&nbsp;", "")
		v = v.rstrip().strip()
		return v

	def InteractiveCLI(self):
		# Ask user what file they would like to load
		file_name = None
		if len(sys.argv) > 1:
			file_name = sys.argv[1]

		self.theSheet = self.loadSheet(file_name)
		self.theSheet.map(self.cleanse_func)

		# Printing header columns
		print("Columns:")
		for column in self.theSheet.row[0]:
			print("- " + column)

	def printThing(self):
		print("testt " + self.test1)

	def __init__(self, userSubmittedCMDLIST=[]):
		print("sheetGod v.0.0.1")
		print("Made by Doug Beney -- https://dougie.io/")

		self.commandList = [
			{
				"Name": "CLI Mode",
				"Description": "Uses CLI instead of GUI.",
				"type": "generic",
				"variants": ("-c", "--cli"),
				"function": self.InteractiveCLI,
			},
		]
		self.commandList = userSubmittedCMDLIST + self.commandList

		self.commands = Commands(sys.argv, self.commandList)
