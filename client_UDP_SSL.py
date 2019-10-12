import socket
import ssl

host='127.0.0.1'
port=80

def client(cafile=None):
    purpose=ssl.Purpose.SERVER_AUTH

    #setting the 'cafile' into a 'None' means that we are not providing any particular
    #CA certificate that must be trusted,
    #and this entails that  a ' create_dafult_context' function
    #will call another function - a 'load_default_certificate' that
    #will take certifciates that are already trusted by our browser

    context=ssl.create_default_context(purpose,cafile=cafile)

    client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #the second parameter of the below function marks this part of the connection as a client
    raw_socket=context.wrap_socket(client,server_hostname=host)

    text='connection request'.encode('ascii')
    raw_socket.sendto(text,(host,port))
    print("All data were sent")

    data,addr=raw_socket.recvfrom_into(1024)
    print("got conenction from:",addr)
    text=data.decode('ascii')
    print("Message:",text)


    raw_socket.close()
    client.close()

client()