import socket,time
import os
from _thread import *
import random
import signal

x = 0
# global thread_count
def Main():
    # thread_count = 0
    s = socket.socket()
    host = ''
    port = 5000
    s.connect((host, port))
    print('Server Started')
    while True:
        c, addr = s.accept()
        msg = 'MARK-ATTENDANCE 20158501'
        c.send(msg.encode())
        print('Connection Established: ' + str(c) + ':' + str(addr))
        print(start_new_thread( clientthread, (c,x)))

def clientthread(conn, x):
    while True:
        y += 1
        data = conn.recv(1024)
        if not data:
            break
        # if data.decode() == 'q':
        #   # print(get_ident())
        #   thread_count -= 1
        #   return 1
        value = int(data.decode())
        if (value is 'ATTENDANCE-SUCCESS'):
            break
        elif (value < x):
            conn.send(less.encode())
        else:
            correct = 'Correct, number of guesses: ' + str(y)
            conn.send(correct.encode())
    conn.close()
if __name__ == '__main__':
    Main()