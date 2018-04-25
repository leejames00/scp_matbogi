import socket

host = socket.gethostname()
print(host)
port = 8001
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientA: Enter message/ Enter exit:").encode()

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE)
    data = tcpClientA.recv(BUFFER_SIZE).decode()
    print(" ClientA received data:", data)
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:").encode()

tcpClientA.close()