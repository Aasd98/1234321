# # 遵循http协议：遵循http协议
# import socket
#
# sock=socket.socket()
# sock.bind(('127.0.0.1',8080))
# sock.listen(5)
# while 1:
#     conn,addr=sock.accept() # 阻塞等待
#     data=conn.recv(1024)
#     print('客户端发送请求信息\n',data)
#
#     conn.send(b'HTTP/1.1 200 ok\r\nserver:yuan\r\n\r\nhelloworld')
#     conn.close()