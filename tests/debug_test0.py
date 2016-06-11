# to test pdb on
from remote_pdb import RemotePdb
RemotePdb("localhost", 4444).set_trace()

def recursive(max):
	if max > 0:
		print "Num: " + str(recursive(max-1))
recursive(3)
