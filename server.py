import socket
s=socket.socket(type=socket.SOCK_DGRAM)
s.bind(('0.0.0.0',1234))
users=[]
def new_user(b):
    if b not in users:
        users.append(b)
    print('New User: '+str(b))
def send(a,b):
    a=a[2:]
    for i in users:
        if i!=b:
            s.sendto(a.encode(),i)
    print('Message Sent')
while True:
    (a,addr)=s.recvfrom(1024)
    a=a.decode()
    if a[:2]=='nu':
        new_user(addr)
    elif a[:2]=='sn':
        send(a,addr)