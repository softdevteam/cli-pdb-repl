import telnetlib
import sys

# Write commands to remote pdb and print output
def interact_pdb():
	while True:
		output = tn.read_until("(Pdb)")
		sys.stdout.write(output + " ")
		sys.stdout.flush()
		command = raw_input()
		tn.write(command + "\n")
		# If user quits then don't wait for (Pdb)
		if isQuitCommand(command):
			break

# Check if command will make the pdb quit
def isQuitCommand(command):
	if (command == "q" or command == "quit"):
		return True
	return False

tn = telnetlib.Telnet("localhost", 4444, 1)
interact_pdb()

