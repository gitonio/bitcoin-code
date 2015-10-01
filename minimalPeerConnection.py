import struct
import socket

import utils
import msgUtils


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(("192.168.59.103", 49020))
sock.connect(("192.168.99.100", 49020))

sock.send(msgUtils.getVersionMsg())

while 1:
    sock.recv(1000) # Throw away data
    print ('got packet')
    
