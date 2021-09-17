import socket
import sys
serversockt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversockt.bind((host,port))
serversockt.listen(5)
while True:
	clientsocket,addr = serversockt.accept()
	print('链接地址： %s' % str(addr))
	msg = '欢迎访问菜鸟教程！' + '\r\n'
	clientsocket.send(msg.encode('utf-8'))
	clientsocket.close()
