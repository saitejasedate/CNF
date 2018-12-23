import socket

remote_server = "google.com"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc: 
    soc.connect((remote_server, 80))
    host = soc.getsockname()[0]

print(host)
def Main():
	port = 5000
	s = socket.socket()
	s.bind((host, port))
	s.listen(2)
	clients = {}
	while True:
		c, addr = s.accept()
		clients[addr] = c
		pressed = 0
		for eachsocket, eachaddrtuple in clients.iteritems():
			print('Recieving data from ' + eachaddrtuple)
			data = c.recv(1024)
			if not data:
				break
			pressed = pressed + 1
			print("From Connected User: " + str(data.decode()))
			data = str(data.decode()).upper()
			print("Sending: " + data)
			c.send(data.encode())
	c.close()

if __name__ == '__main__':
	Main()