import socket
import time
import sys
import time
from base_camera import BaseCamera

config={'ip':'10.164.33.222',
			'port':5001}

class Camera(BaseCamera):
    mySocket = socket.socket()
    mySocket.connect((config['ip'],config['port']))
 
    @staticmethod
    def frames():
        while True: 
            message='acquire'
            Camera.mySocket.sendall(message.encode())
            #sys.stdout.flush()
            
            data = Camera.mySocket.recv(100000)
            yield data
