# to test pdb on
from remote_pdb import RemotePdb
RemotePdb("localhost", 4444).set_trace()

def getLongestName(names):
	longestName = ""
	topLen = 0
	for name in names:
		if len(name) > topLen:
			longestName = name
			topLen = len(name)
	return longestName

people = ["Tom", "Stan", "Miles", "Laura", "Maggie", "Eddie", "Claus"]
print getLongestName(people)
