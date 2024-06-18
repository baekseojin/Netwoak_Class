from socket import *

s_ip = 'localhost'
s_port = 12345
s_addr = (s_ip, s_port)

s_sock = socket(AF_INET, SOCK_DGRAM) 
s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR) # 데이터를 계속 주고받기 위해서(연결된 것을 끊지 않는다)

s_sock.bind(s_addr)

data, c_addr = s_sock.recvfrom(1024) 

while True: 
    if data.decode('utf-8') == 'q':
        break
    print('수신자 client addr : ', c_addr)
    print('수신된 자료는 : ', data.decode('utf-8'))
    print()
    s_sock.sendto(data, c_addr) # encode 할 필요 없음 (12번째 줄에서 이미 인코드된 자료를 받음)
    data, c_addr = s_sock.recvfrom(1024)

s_sock.close()
