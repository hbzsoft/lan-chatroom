import socket
from threading import Thread
s=socket.socket(type=socket.SOCK_DGRAM)
s.bind(('0.0.0.0',1236))
print('LAN Chat Room v1.0 by Han Bangze')
print('All rights reserved.')
server_ip=input('Please input the IP of the server: ')
s.sendto(b'nu',(server_ip,1234))
nickname=input("Please input your nickname: ")
s.sendto(('sn'+'\033[93m'+'System Message: User '+nickname+' entered the room.').encode(),(server_ip,1234))
chatting=True
class receiving(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global s, chatting
        while chatting:
            try:
                print((s.recvfrom(2048)[0].decode()))
            except ConnectionResetError:
                chatting = False
recv_thread = receiving()
recv_thread.start()
while chatting:
    data = input()
    if data=='quit':
        exit()
    data = nickname + ': '+ data
    data = "\033[92m" + data
    if len(data) > 2046:
        print("Error: message too long(%d bytes)"%len(data))
        continue
    data='sn'+data
    data=data.encode()
    s.sendto(data,(server_ip,1234))
