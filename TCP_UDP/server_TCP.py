import socket
import threading
import time

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...'%addr)
    sock.send(b'Welcom!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('没想到吧,%s,\n Bye'%data.decode('utf-8')).encode('utf-8'))
        #sock.send(('Bye'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' %addr)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.1.103',9999))#监听端口
s.listen(5)#参数指定等待连接的最大数量
print('Waiting for connection...')

while True:
    sock, addr=s.accept()#接收连接
    t=threading.Thread(target=tcplink, args=(sock,addr))#创建线程
    t.start()

