import socket

PORT = 5050
#SERVER = ''
SERVER = socket.gethostbyname (socket.gethostname ())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = '!DISCONNECT'

client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
client.connect (ADDR)

def send (messages):
    message = messages.encode (FORMAT)
    messageLength = len (message)
    sendLength = str (messageLength).encode (FORMAT)
    sendLength += b' ' * (HEADER - len (sendLength))
    client.send (sendLength)
    client.send (message)
    print (client.recv (2045).decode (FORMAT))

if __name__ == '__main__':
    send ('Hello World')
    send (DISCONNECT_MESSAGE)
