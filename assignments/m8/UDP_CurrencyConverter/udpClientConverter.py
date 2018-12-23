import socket

remote_server = "google.com"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc: 
    soc.connect((remote_server, 80))
    host = soc.getsockname()[0]

def Main():
	port = 5101
	server = (host, 5000)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	message = input('-->')
	while True:
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		print('Data Recieved from Server: ' + str(data.decode()))
		message = input('-->')
	s.close()
if __name__ == '__main__':
	Main()