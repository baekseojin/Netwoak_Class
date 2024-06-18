from socket import *  # socket.accept, socket.bind 등의 함수를 socket 안적고도 실행할 수 있게 하는 구문

s_ip = 'localhost' # localhost : 자기 자신 컴퓨터를 부르는 네트워크 아이디 (127.0.0.1)
s_port = 9999
s_addr = (s_ip, s_port) # 리스트는 수정이 가능한데 튜플은 수정이 불가능함

s_sock = socket(AF_INET, SOCK_STREAM) # AF_INET : IPv4를 의미, SOCK_STREAM : TCP 프로토콜 => socket을 만드는 구문
s_sock.bind(s_addr) # socket에다가 bind
s_sock.listen(2) # 동시에 접속할 수 있는 클라이언트 숫자(2)

client, c_addr = s_sock.accept() 
print(c_addr, 'is connected')

data1 = 'Thank you for connecting'
client.send(data1.encode('utf-8'))
data2 = 'Receive data from client : '
print(data2, client.recv(1024).decode('utf-8'))

client.close()
s_sock.close()






