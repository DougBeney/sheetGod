class Arguments():
	def cmd_help(self):
		print("Command options:")
		print("---------------")
		for cmd in self.commandList:
			print(str(cmd['variants']))
			print("-- " + cmd['name'])
			print("-- " + cmd['description'])
			print("---------------")

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
		# Process variables first
		for cmd in self.argv:
			if cmd is not self.argv[0]:
				# Looping through commands inputed
				cmd = str(cmd)
				if "=" in cmd:
					splitcmd = cmd.split("=")
					self.processCommand(splitcmd[0], splitcmd[1])
		# Then process functions
		for cmd in self.argv:
			if cmd is not self.argv[0]:
				# Looping through commands inputed
				cmd = str(cmd)
				if "=" not in cmd:
					self.processCommand(cmd)

	def addCommands(self, cmds):
		self.commandList = self.commandList + cmds

	# Command List
	def __init__(self, argv, command_list):
		self.commandList = [
			{
				"name": "Help",
				"description": "Shows the commands of sheetGod",
				"type": "generic",
				"variants": ("-h", "--help"),
				"function": self.cmd_help,
			},
		]
		self.commandList = self.commandList + command_list
		self.argv = argv
		self.checkCommands()
