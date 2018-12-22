import socket
import csv

def Main():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        s = socket.socket()
        host = '127.0.0.1'
        port = 5000
        s.bind((host, port))
        s.listen()
        c, addr = s.accept()
        value = c.recv(1024).decode()
        if value is 'MARK-ATTENDANCE':
            for row in csv_reader:
                if value is row:
                    break

if __name__ == '__main__':
    Main()