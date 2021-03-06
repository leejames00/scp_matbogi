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
            node_name, json_msg = msg.split(" ")[0], ''.join(msg.split(" ")[1:])
            msg_list.insert(tkinter.END, msg)

            if is_json(json_msg):
                node.handle_message(json_msg) # receive vote and handle
                msg = json.loads(json_msg)
                peerID, SCPenv = msg['nodeID'], msg['msgType']

                if node.voted: # if voted is not empty
                    # [TODO] check validity of vote (if valid)
                    new_message = json.dumps({'nodeID': node.nodeID, 'msgType': 'vote'}) # send my vote
                    node.handle_message(new_message)
                    client_socket.send(bytes(new_message, "utf8"))
                    print("sending vote message")
                if node.accepted: # if accepted is not empty
                    new_message = json.dumps({'nodeID': node.nodeID, 'msgType': 'accept'})
                    node.handle_message(new_message)
                    client_socket.send(bytes(new_message, "utf8"))
                    print("sending accept message")
                if node.confirmed: # if confirmed is not empty
                    new_message = json.dumps({'nodeID': node.nodeID, 'msgType': 'confirm'})
                    node.handle_message(new_message)
                    client_socket.send(bytes(new_message, "utf8"))
                    print("sending confirm message")
                #node.handle_message(new_message)
                #client_socket.send(bytes(new_message, "utf8"))

        except OSError:
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.

    if msg == 'start':
        msg = json.dumps({'nodeID': node.nodeID, 'msgType': 'vote'})
        node.vote(msg)

    if msg == 'history':
        msg_list.insert(tkinter.END, node.voted)
        msg_list.insert(tkinter.END, node.accepted)
        msg_list.insert(tkinter.END, node.confirmed)


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

HOST = '127.0.0.1'
PORT = 8000

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()