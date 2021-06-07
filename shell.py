import processor
from timeit import timeit

class RequestExit(Exception):
	pass

print("// ConfusedScript Shell //")
print("Use \"exit ()\" (Without double quotes) or Press CTRL+C to exit")

printNone = False

try:
	while True:
		command = input("ConfusedScript > ")
		if(command.startswith("xi (")): raise RequestExit
		if(command.startswith("#df")):
			scommand = command.split()
			try:
				if scommand[1] == "shellSettings":
					if scommand[2] == "printWhenReturnNone":
						if scommand[3] == "true":
							printNone = True
							continue
						elif scommand[3] == "false":
							printNone = False
							continue
			except IndexError:
				print("IS: The Option you wanted to settings is required.")
		out = processor.execute(command)
		if not printNone:
			if out == None:
				continue
			else: print(out)
		else: print(out)
except KeyboardInterrupt:
	print("\nKeyboard interrupt recieved. Exiting...")
except RequestExit:
	print("Exiting requested. Exiting...")
except Exception:
	from traceback import print_exc
	print_exc()