import socket
import time
from threading import *


def show(ip, port):
    myp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, myp)
    # ip = "192.168.99.106"
    # port = 6789
    s.bind((ip, port))
    while True:
        x = s.recvfrom(1024)
        print('Received Message : ',x[0].decode())
        time.sleep(2 / 10)

def reply(ip2, port2):
    myp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, myp)
    while True:
        msg = input()
        # s.sendto(msg.encode(), ("192.168.99.105", 3456))
        s.sendto(msg.encode(), (ip2, port2))
        print('Your Message : ', msg)
        time.sleep(0.2)

ip = input('Enter your IP address : ')
port = int(input('Enter your port number : '))
ip2 = input("Enter Friend's IP address : ")
port2 = int(input("Enter Friend's port number : "))

t1 = Thread(target=reply, args=(ip2, port2))
t2 = Thread(target=show, args=(ip, port))

t1.start()
t2.start()
