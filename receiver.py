import socket
import time
from threading import *


def reply():
    
    myp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, myp)
    while True:
        msg = input()
        s.sendto(msg.encode(), ("192.168.99.106", 6789))
        print('Your Message : ', msg)
        time.sleep(0.2)

def show():

    myp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, myp)
    ip = "192.168.99.105"
    port = 3456
    s.bind((ip, port))
    while True:
        x = s.recvfrom(1024)
        print('Received Message : ', x[0].decode())
        time.sleep(2 / 10)


t1 = Thread(target=show)
t2 = Thread(target=reply)

t1.start()
t2.start()

