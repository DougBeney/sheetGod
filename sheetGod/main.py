import os
import sys
import platform

from .sheet import Sheet
from .arguments import Arguments


class sheetGod():
	AllowedCommands = [
		"help",
		"show",
		"open",
		"quit",
		"clear",
		"cls"
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
		self.sheet.setManualCommands([
			{
				"name": "exit / quit",
				"help": "Use this to quit sheetGod CLI",
			},
			{
				"name": "clear / cls",
				"help": "Use this command to clear the console."
			}
		])

		while self.CLI_IS_RUNNING:
			# CLI Interface Loop
			cmd = input("$ ")

			cmdArray = cmd.split(" ")
			mainCommand = cmdArray[0]
			cmdArray.remove(cmdArray[0])

			# If user typed exit or quit, exit immediately.
			if mainCommand in self.AllowedCommands:
				if mainCommand == "exit" or mainCommand == "quit":
					print("Goodbye!")
					self.CLI_IS_RUNNING = False
					break
				elif mainCommand == "clear" or mainCommand == "cls":
					operating_system = platform.system()
					clear_command = "clear"
					if "Windows" in operating_system:
						clear_command = "cls"
					os.system(clear_command)
				elif cmd != "":
					try:
						getattr(self.sheet, mainCommand)(*cmdArray)
					except AttributeError as err:
						print(err)
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

		self.commands = Arguments(sys.argv, self.commandList)
