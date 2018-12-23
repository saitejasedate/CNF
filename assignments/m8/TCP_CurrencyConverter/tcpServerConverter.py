import socket

remote_server = "google.com"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc: 
    soc.connect((remote_server, 80))
    host = soc.getsockname()[0]

def Main():
	port = 5000
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, addr = s.accept()
	dict = {'Dollar': 1, 'INR': 0, 'Pounds': 2, 'Yen': 3}
	print("Connection from: " + str(addr))
	matrix = [[1.0, 0.014, 0.011, 1.58], [72.1, 1.0, 0.79, 112.60], [89.98, 1.26, 1.0, 142.17], [0.63, 0.0089, 0.0070, 1.0]]
	while True:
		data = c.recv(1024)
		if not data:
			break
		data = data.decode()
		datalist = data.split()
		value = float(matrix[dict[datalist[1]]][dict[datalist[4]]])
		value = int(datalist[2]) * value
		print("From Connected User: " + str(value))
		print("Sending: " + str(value))
		c.send(str(value).encode())
	c.close()

if __name__ == '__main__':
	Main()