import socket

class Client:

	def __init__(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(("localhost", 2384))
		
		while 1:
			sock.send("Hello!!!!")
			s = sock.recv(1024)
			print(s)

c = Client()
