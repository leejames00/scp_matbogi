import socket

def receive():
    host = "127.0.0.1"
    port = 5001

    s = socket.socket()
    s.bind((host, port))
    print("bindend")
    s.listen(1)
    while True:
        c, addr = s.accept()
        while True:
            data = c.recv(1024)
            if not data:
                break
            print(data)
            c.send(bytes("Ordre registreret", "utf-8"))
        c.close()

def send():
    host = "127.0.0.1"
    port = 5002

    s = socket.socket()
    s.connect((host, port))
    print("connected")
    s.send("Test", "utf-8")

    data = s.recv(1024)
    data = str(data, "utf-8")
    s.close()


send()