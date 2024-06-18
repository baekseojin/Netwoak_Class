from socket import *  # socket.accept, socket.bind 등의 함수를 socket 안적고도 실행할 수 있게 하는 구문

s_ip = 'localhost'
s_port = 9999
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_STREAM) # AF_INET : IPv4를 의미, SOCK_STREAM : TCP 프로토콜 => socket을 만드는 구문
c_sock.connect(s_addr)

data1 = 'Received data from server : '
print(data1, c_sock.recv(1024).decode('utf-8'))
data2 = 'Hello, TCP Server'
c_sock.send(data2.encode('utf-8'))

c_sock.close()

