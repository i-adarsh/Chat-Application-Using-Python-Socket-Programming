import socket
import sys
import time
from threading import *


def receiver(ip, port):
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

def sender(ip2, port2):
    myp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, myp)
    while True:
        msg = input()
        # s.sendto(msg.encode(), ("192.168.99.105", 3456))
        s.sendto(msg.encode(), (ip2, port2))
        print('Your Message : ', msg)
        time.sleep(0.2)

sys.stdout.write("Enter your IP address: ")
sys.stdout.flush()
ip = sys.stdin.readline()
port = int(input('Enter your port number : '))

sys.stdout.write("Enter Friend's IP address : ")
sys.stdout.flush()
ip2 = sys.stdin.readline()
port2 = int(input("Enter Friend's port number : "))

t1 = Thread(target=sender, args=(ip2, port2))
t2 = Thread(target=receiver, args=(ip, port))

t1.start()
t2.start()
