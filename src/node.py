
class Node:
    def __init__(self, nodeID):
        self.nodeID = nodeID
        self.threshold = 4
        self.voted = dict()
        self.accepted = dict()
        self.confirmed = dict()

    def __repr__(self):
        return '<Node: %s>' % self.nodeID

    def set_qset(self, node):
        self.qset.append(node)

    def set_init(self):
        self.voted = dict()
        self.accepted = dict()
        self.confirmed = dict()

    def vote(self, message):
        #parse(message) = nodeID, SCPenv
        # store in voted = {SCPenv: nodeID}
        if message not in self.voted:
            self.voted[message] = 1
        else:
            self.voted[message] += 1
        if self.voted[message] >= self.threshold:
            self.voted.pop(message)
            self.accept(message)

    def accept(self, message):
        if message not in self.accepted:
            self.accepted[message] = 1
        else:
            self.accepted[message] += 1
        if self.accepted[message] >= self.threshold:
            self.accepted.pop(message)
            self.confirm(message)

    def confirm(self, message):
        if message not in self.confirmed:
            self.confirmed[message] = 1
        else:
            self.confirmed[message] += 1
        if self.confirmed[message] >= self.threshold:
            return "message is confirmed"

    def send_message(self, name):
        print("sent message")

    def broadcast(self):
        for node in self.qset:
            self.send_message(node.name)

    def receive_message(self, name):
        print("receivemessage")

    def handle_msg(self, msg):
        if msg == 'vote':
            self.vote(msg)
            print(self.voted)
        elif msg == 'accept':
            self.accept(msg)
        elif msg == 'confirm':
            self.confirm(msg)
        else:
            print(msg)






