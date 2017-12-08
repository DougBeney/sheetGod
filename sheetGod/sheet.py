from inspect import signature
import pyexcel


class Sheet():
	sheet = None
	AllowedCommands = None

	def open(self, file_name=None):
		if file_name:
			try:
				sheet = pyexcel.get_sheet(file_name=file_name)
			except:
				print("Can't read file [%s]..." % file_name)
				return False
			else:
				cleanse_func = lambda v: str(v).replace("&nbsp;", "").rstrip().strip()
				sheet.map(cleanse_func)
				self.sheet = sheet
				return True
		else:
			print("Please provide a filename when using the 'open' command.")

	def help(self, item=None):
		print("Commands:")
		# for cmd in self.AllowedCommands:
		# 	print(signature(self.fuck))
		members = [attr for attr in dir(Sheet)]
		for item in members:
			if item in self.AllowedCommands:
				parameters = str(signature(getattr(self, item)))
				parameters = parameters.split("=")
				if len(parameters) > 1:
					parameters[0] += ")"
				theItem = parameters[0]
				theItem = theItem.replace("()", "")

				command_details = item + " " + str(theItem)

				print("  * " + command_details)

	def show(self):
		if self.sheet:
			print(self.sheet)
		else:
			print("None")

	def setSheet(self, sheet):
		self.sheet = sheet

	def __init__(self, AllowedCommands):
		self.AllowedCommands = AllowedCommands
