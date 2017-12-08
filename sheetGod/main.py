import sys

from .sheet import Sheet
from .commands import Commands


class sheetGod():
	AllowedCommands = [
		"help",
		"show",
		"open"
	]
	sheet = Sheet(AllowedCommands)

	def InteractiveCLI(self):
		print("sheetGod v.0.0.1 (by Doug Beney)")

		print("\n")
		print("* Website: https://sheetgod.dougie.io")
		print("* Docs: https://sheetgod.dougie.io/docs")
		print("* Contact the dev: https://sheetgod.dougie.io/contact")
		print("\n")

		self.CLI_IS_RUNNING = True

		while self.CLI_IS_RUNNING:
			# CLI Interface Loop
			cmd = input("$ ")
			# If user typed exit or quit, exit immediately.
			if cmd == "exit" or cmd == "quit":
				print("Goodbye!")
				self.CLI_IS_RUNNING = False
				break

			cmdArray = cmd.split(" ")
			mainCommand = cmdArray[0]
			cmdArray.remove(cmdArray[0])
			# Run command in Sheet class

			if mainCommand in self.AllowedCommands:
				if cmd != "":
					try:
						getattr(self.sheet, mainCommand)(*cmdArray)
					except AttributeError as err:
						print("Nope.")
						getattr(self.sheet, "help")(cmd)
			else:
				print("Command does not exist.")
				print("¯\_(ツ)_/¯")
				print("Type 'help' for a list of commands.")

		# Printing header columns
		# print("Columns:")
		# for column in self.theSheet.row[0]:
		# 	print("- " + column)

	def __init__(self, userSubmittedCMDLIST=[]):
		self.commandList = [
			{
				"name": "CLI Mode",
				"description": "Uses CLI instead of GUI.",
				"type": "generic",
				"variants": ("-c", "--cli"),
				"function": self.InteractiveCLI,
			},
			{
				"name": "Open File",
				"description": "(Example usage: '--open=myfile.csv')",
				"type": "variable",
				"variants": ("-o", "--open"),
				"function": self.sheet.open,
			},
		]
		self.commandList = userSubmittedCMDLIST + self.commandList

		self.commands = Commands(sys.argv, self.commandList)
