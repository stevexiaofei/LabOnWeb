import socket
import time
import sys
import cv2
config={'ip':'127.0.0.1',
			'port':5001}
def initialize():
	camera = cv2.VideoCapture(0)
	mysocket = socket.socket()
	mysocket.bind((config['ip'],config['port']))
	mysocket.listen(1)
	conn,addr = mysocket.accept()
	print('conneted from: {}'.format(addr))
	return camera,mysocket,conn
	
def main():
	imgs = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
	camera,mysocket,conn = initialize()
	while(True):
		data = conn.recv(1024).decode()
		if not data:
			continue
		reply=str(data)
		if reply=='acquire':
			#data_tobe_send=cv2.imencode('.jpg', camera.read()[1])[1].tobytes()
			reply
			data_tobe_send=imgs[int(time.time()) % 3]
			conn.send(data_tobe_send)
			time.sleep(1)
		elif reply=='suspend':
			continue
		#else:
		#conn.close()
if __name__=='__main__':
	main()
	