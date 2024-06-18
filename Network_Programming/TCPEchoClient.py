from socket import * # socket.accept, socket.bind 등의 함수를 socket 안적고도 실행할 수 있게 하는 구문

s_ip = 'localhost'
s_port = 12345
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_STREAM) # 소켓 연결
c_sock.connect(s_addr) # connect 

while True:
    inputData = input("입력 문자열 : ")
    c_sock.send(inputData.encode('utf-8'))
    print(c_sock.recv(1024).decode('utf-8'))

    if inputData == '1':
        print("송신 종료")
        break
    
c_sock.close()




