import socket
import subprocess

class Server:

	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(("localhost", 2384))
		self.sock.listen(5)

	def accept_connections(self):
		while 1:
			# accept socket
			(clientsock, address) = self.sock.accept()
			# do something with socket
			while 1:
				try:
					s = clientsock.recv(1024)
					print(s)
					clientsock.send("Hello client.")
				except:
					break

s = Server()
s.accept_connections()
