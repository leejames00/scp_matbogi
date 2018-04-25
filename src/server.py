import socket
from threading import Thread
#from SocketServer import ThreadingMixin

# class Client
# s = socket.socket()
# print("socket created")
#
# port = 12345
#
# s.bind(("localhost", 8000))
# print("socket binded to %s" %port)
#
# s.listen(5)
# print("socket is listening")
#
# while True:
#     c, addr = s.accept()
#     print("got connection from", addr)
#
#     c.send("Thank you for connecting")
#
#     c.close()

# class ClientThread(Thread):
#
#     def __init__(self, ip, port):
#         Thread.__init__(self)
#         self.ip = ip
#         self.port = port
#         print("[+] New thread started for "+ip+":"+str(port))
#
#
#     def run(self):
#         while True:
#             data = conn.recv(2048)
#             if not data: break
#             print("received data:", data)
#             conn.send(data)  # echo
#
# TCP_IP = '127.0.0.1'
# TCP_PORT = 8000
# BUFFER_SIZE = 20  # Normally 1024, but we want fast response
#
#
# tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# tcpsock.bind((TCP_IP, TCP_PORT))
# threads = []
#
# while True:
#     tcpsock.listen(4)
#     print("Waiting for incoming connections...")
#     (conn, (ip,port)) = tcpsock.accept()
#     newthread = ClientThread(ip,port)
#     newthread.start()
#     threads.append(newthread)
#
# for t in threads:
#     t.join()

TCP_IP = '0.0.0.0'
TCP_PORT = 8001
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((TCP_IP, TCP_PORT))
# s.listen(1)
#
# conn, addr = s.accept()
# print('Connection address:', addr)
# while 1:
#     data = conn.recv(BUFFER_SIZE)
#     if not data: break
#     print ("received data:", data)
#     #conn.send(data)  # echo
#     if "/version" in data:
#         conn.send(b"Demo versionn")
#
#     if "/echo" in data:
#         data = data.replace("/echo","")
#         conn.send(data + "n")
#
# conn.close()


class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("new server started with ip" + ip + ":" + str(port))

    def run(self):
        while True :
            data = conn.recv(2048).decode()
            print("Server received data:", data)
            MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:").encode()
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE)  # echo

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    print("Waiting for connections")
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    print("newthread started")
    threads.append(newthread)

for t in threads:
    t.join()


