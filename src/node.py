import json

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
        message = json.loads(message)
        nodeID, SCPenv = message['nodeID'], message['msgType']
        # store in voted = {SCPenv: nodeID}
        if SCPenv not in self.voted:
            self.voted[SCPenv] = 1 # [nodeID]
        else:
            self.voted[SCPenv] += 1 #.append(nodeID)
        if self.voted[SCPenv] >= self.threshold:
            self.voted.pop(SCPenv)
            print("vote goes to accept")
            self.accept(SCPenv)

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

    def handle_SCPenv(self, message):
        nodeID, SCPenv = message.split(" ")[0], message.split(" ")[1]
        if SCPenv == 'vote':
            self.vote(message)
            print(self.voted)
        elif SCPenv == 'accept':
            self.accept(message)
        elif SCPenv == 'confirm':
            self.confirm(message)
        else:
            print(SCPenv)






