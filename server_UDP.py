import socket

host='127.0.0.1'
port=80

def server():
    server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind((host,port))
    print("[*] Listening...")
    data,addr=server.recvfrom(1024)
    print("got connection from:",addr)
    text=data.decode('ascii')
    print("Message:",text)
    text=' initializing...'.encode('ascii')
    server.sendto(text,(host,port))
    print("data were sent")

    server.close()

server()