from socket import * # socket.accept, socket.bind 등의 함수를 socket 안적고도 실행할 수 있게 하는 구문

s_ip = 'localhost' # localhost : 자기 자신 컴퓨터를 부르는 네트워크 아이디 (127.0.0.1)
s_port = 12345 # 포트 번호 지정(12345)
s_addr = (s_ip, s_port) # 튜플로 묶기 (수정이 불가능하다)

s_sock = socket(AF_INET, SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = socket을 만드는 구문
s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # 데이터를 계속 주고받기 위해서(연결된 것을 끊지 않는다)

s_sock.bind(s_addr) 
s_sock.listen(2) # 동시에 접속할 수 있는 클라이언트 숫자(2) 

client, c_addr = s_sock.accept()
print(c_addr, "Now Connected")

data = "dummy"

while len(data): # 문자열의 길이만큼(5)
    data = client.recv(1024).decode('utf-8') # accept를 하면 가상의 통로(소켓, client의 길)가 만들어지고 코드 해석 
    if data == 'q':
        print("\n수신종료")
        break
    print('수신된 Data : ', data)
    client.send(data.encode('utf-8')) # 코드 암호화 

client.close()
s_sock.close()