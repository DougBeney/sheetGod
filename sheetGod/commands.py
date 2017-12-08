class Commands():
	def cmd_help(self):
		print("Commands for sheetGod:")
		for cmd in self.commandList:
			print(cmd)

	def processCommand(self, cmd, value=None):
		for commandListItem in self.commandList:
			for variation in commandListItem['variants']:
				if variation == cmd:
					if commandListItem['type'] == 'variable':
						commandListItem['function'](value)
					else:
						commandListItem['function']()
					return

	def checkCommands(self):
		for cmd in self.argv:
			if cmd is not self.argv[0]:
				# Looping through commands inputed
				cmd = str(cmd)
				if "=" in cmd:
					splitcmd = cmd.split("=")
					self.processCommand(splitcmd[0], splitcmd[1])
				else:
					self.processCommand(cmd)

	def runCommand(self, cmd, value):
		print("Toggle Type")

	# Command List
	# Note: Types of commands availible: [toggle, variable, detail]

	def __init__(self, argv, command_list):
		self.commandList = [
			{
				"Name": "Help",
				"Description": "Shows the commands of sheetGod",
				"type": "generic",
				"variants": ("-h", "--help"),
				"function": self.cmd_help,
			},
		]
		self.commandList = self.commandList + command_list
		self.argv = argv
		self.checkCommands()
