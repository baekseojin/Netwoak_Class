from socket import *
 
s_ip = 'localhost'
s_port = 12347
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_DGRAM)
 
inputData = input('입력 문자열 : ')
c_sock.sendto(inputData.encode('utf-8'), s_addr)
 
while inputData != 'q':
    data, addr = c_sock.recvfrom(1024)
 
    print('Echoed data : ', data.decode('utf-8'))
    inputData = input('입력 문자열 : ')
    c_sock.sendto(inputData.encode('utf-8'), s_addr)
 
c_sock.close()
