import socket
import select

def create_socket(TCP_PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', TCP_PORT))
    print("created socket", server_socket)
    server_socket.listen(1)

    return server_socket


def main():

    read_list = []

    for TCP_PORT in range(8000,8005):
        read_list.append(create_socket(TCP_PORT))

    while True:
        readable, writable, exceptional = select.select(read_list, [], read_list)
        for s in readable:
            if s is server_socket:
                #print "client connected"
                client_socket, address = server_socket.accept()
                read_list.append(client_socket)
            else:
                # One of the tcp clients
                data = s.recv(1024)
                if not result:
                    s.close()
                    read_list.remove(s)
                    #print "client disconnected"

if __name__ == "__main__":
    main()