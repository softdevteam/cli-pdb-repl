# to test pdb on
from remote_pdb import RemotePdb
RemotePdb("localhost", 4444).set_trace()

# bunch of functions to test pdb commands that do something with the stack frames (up, down, where)
def func1(num):
	func2(num-1)

def func2(num):
	func3(num-1)

def func3(num):
	func4(num-1)

def func4(num):
	func5(num-1)

def func5(num):
	func1(num-1)
	
func1(10)
