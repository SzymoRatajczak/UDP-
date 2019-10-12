import socket
import ssl

host='127.0.0.1'
port=80

def server(cafile=None):
    purpose=ssl.Purpose.CLIENT_AUTH
    context=ssl.create_default_context(purpose,cafile=cafile)

    server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("[* listening]")

    #the second parameter of the below function marks this part of the connection as a server
    raw_socket=context.wrap_socket(server,server_side=True)

    data,addr=raw_socket.recvfrom(1024)
    print("got connection from:",addr)
    text=data.decode('ascii')
    print("Message:",text)

    text='response'.encode('ascii')
    raw_socket.sendto(text,(host,port))
    print("All data were sent")

    server.close()
    raw_socket.close()

server()