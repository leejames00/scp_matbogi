from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from node import Node
import json
import random

nodeID = random.randint(1,100)
node = Node(nodeID)

def is_json(msg):
    try:
        json_object = json.loads(msg)
    except ValueError:
        return False
    return True

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            # need to parse message into node:vote
            # all messages are encoded in json /
            #if message is encoded in json:
            if is_json(msg):
                print("this is json format")
                msg = json.loads(msg)
                peerID, SCPenv = msg['nodeID'], msg['msgType']
                print(msg)
            # then, store the message into node.voted
                new_message = json.loads({'nodeID': node.nodeID, 'msgType': SCPenv})
                node.handle_SCPenv(SCPenv)
                print("i am sending", new_message)
                client_socket.send(bytes(new_message, "utf8"))
                print("voted: ", node.voted)
                print("accepted: ", node.accepted)
                print("confirmed: ", node.confirmed)
                print("i just sent", SCPenv)

        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    # msg = json.puts({'nodeid': self.nodeid, 'msgtype': 'hello'}) #messag are all encoded in json


    if msg == 'vote':
        print(msg)
        print(node.nodeID)
        msg = json.dumps({'nodeID': node.nodeID, 'msgType': 'vote'})
        print(msg)
        node.vote(msg)
    # print("voted: ", node.voted)
    # print("accepted: ", node.accepted)
    # print("confirmed: ", node.confirmed)
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Node")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = '127.0.0.1'
PORT = 8000

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()