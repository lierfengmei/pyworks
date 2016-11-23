
# import socket

# #创建一个socket
# #socket.AF_INET 指定IPv4协议，
# #socket.SOCK_STREAM 指定使用面向流的TCP协议
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接
# s.connect(('www.sina.com.cn',80))

# s.send(b'GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')

# buffer = []

# while True:
# 	# 每次最多接收1k字节：
# 	d = s.recv(1024)
# 	if d:
# 		buffer.append(d)
# 	else:
# 		break;
# data = b''.join(buffer)

# s.close()

# #分离http头和网页，将http头打印出来，网页内容保存到文件
# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# #把接收到数据写入文件
# with open('sina.html','wb') as f:
# 	f.write(html)



#------------------------服务器端口------------------------
#服务器要能够区分一个Socket连接是和哪个客户绑定的，一个Socket依赖4项：
#服务器地址、服务器端口、客户端地址、客户端端口——>唯一的Socket

import socket
import threading
import time


def tcplink(sock,addr):
	print('Accept new connection from %s:%s' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s：%s closed!' % addr)



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('Waiting for connection...')

while True:
	#接受一个新连接
	sock,addr = s.accept()
	#创建新线程来处理TCP连接
	t = threading.Thread(target = tcplink, args = (sock,addr))
	t.start()

