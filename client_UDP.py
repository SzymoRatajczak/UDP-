import socket

host='127.0.0.1'
port=80
def client():
    client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text='connection request'.encode('ascii')
    client.sendto(text,(host,port))
    print("All data were sent")
    data,addr=client.recvfrom(1024)
    print("got connection from the server under the address:",addr)
    text=data.decode('ascii')
    print("Message:",text)

    client.close()

client()