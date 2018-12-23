import socket
import os
from threading import *
import time
import signal
remote_server = "google.com"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc: 
    soc.connect((remote_server, 80))
    host = soc.getsockname()[0]
print(host)

def Main():
    port = 5001
    s = socket.socket()
    s.bind((host,port))
    print('server started: ' + str(os.getpid()))
    s.listen(10)
    client_list = []
    name_conn = {}
    while True:
        c, addr = s.accept()
        c.send(wel.encode())
        c.send('Enter your Name: '.encode())
        conn_name = c.recv(1024)
        print('Connected User: ' + conn_name.decode())
        name_conn[c] = str(conn_name.decode())
        client_list.append(c)
        for con in client_list:
            if c != con:
                con.send((name_conn[c] + ' is Connected.').encode())
        Thread(target = chatclients, args = (c, addr, client_list, name_conn)).start()
    s.close()
    
def check():
    print(active_count())
    if (active_count() == 2):
        print('Waiting for Connections....')
        time.sleep(10)
        if (active_count() == 2):
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)

def chatclients(c, addr, client_list, name_conn):
    while True:
        try:
            message = (c.recv(1024)).decode()
            print(name_conn[c] + '<-->' + message)
            if message != 'x' and c in client_list:
                for client in client_list:
                    if c != client:
                        try:
                            name = name_conn[c]
                            client.send((name + '-->' + message).encode())
                        except:
                            c.close()
                            remove(c, client_list)
            else:
                c.send(('Do you want to Exit?(Y/N)').encode())
                if ((c.recv(1024)).decode() == 'Y'):
                    for con in client_list:
                        if c != con:
                            con.send((name_conn[c] + ' is disconnected. Users online: ' + str(active_count() - 2)).encode())
                    c.send('Disconnect'.encode())
                    remove(c,client_list)
                    check()
                    return 1
        except:
            continue
    c.close()

def remove(c, client_list):
    if c in client_list:
        client_list.remove(c)

if __name__ == '__main__':
    Main()