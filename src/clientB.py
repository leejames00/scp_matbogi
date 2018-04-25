import socket

host = socket.gethostname()
print(host)
port = 8001
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientB: Enter message/ Enter exit:").encode()

tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientB.connect((host, port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE)
    data = tcpClientB.recv(BUFFER_SIZE).decode()
    print(" ClientB received data:", data)
    MESSAGE = input("tcpClientB: Enter message to continue/ Enter exit:").encode()

tcpClientB.close()