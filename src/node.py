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

    def self_vote(self, SCPenv):
        message = json.dumps({'nodeID': self.nodeID, 'msgType': 'vote'})
        self.vote(message)

    def self_accept(self, SCPenv):
        message = json.dumps({'nodeID': self.nodeID, 'msgType': 'accept'})
        self.accept(message)

    def self_confirm(self, SCPenv):
        message = json.dumps({'nodeID': self.nodeID, 'msgType': 'confirm'})
        self.confirm(message)

    def vote(self, message):
        message = json.loads(message)
        nodeID, SCPenv = message['nodeID'], message['msgType']

        if SCPenv not in self.voted:
            self.voted[SCPenv] = set() # unique set [nodeID]

        self.voted[SCPenv].add(nodeID)

        print("nodeID: added", self.nodeID)
        print("voted: ", self.voted)

        if len(self.voted[SCPenv]) == self.threshold:
            #self.voted.pop(SCPenv)
            self.self_accept(SCPenv)

    def accept(self, message):
        message = json.loads(message)
        nodeID, SCPenv = message['nodeID'], message['msgType']

        if SCPenv not in self.accepted:
            self.accepted[SCPenv] = set()

        self.accepted[SCPenv].add(nodeID)

        if len(self.accepted[SCPenv]) == self.threshold:
            #self.accepted.pop(SCPenv)
            self.self_confirm(SCPenv)

    def confirm(self, message):
        message = json.loads(message)
        nodeID, SCPenv = message['nodeID'], message['msgType']

        if SCPenv not in self.confirmed:
            self.confirmed[SCPenv] = set()

        self.confirmed[SCPenv].add(nodeID)

        if len(self.confirmed[SCPenv]) == self.threshold:
            print(SCPenv + " is confirmed")

    def handle_message(self, message):
        json_obj = json.loads(message)
        nodeID, SCPenv = json_obj['nodeID'], json_obj['msgType']
        if SCPenv == 'vote':
            self.vote(message)
        elif SCPenv == 'accept':
            self.accept(message)
        elif SCPenv == 'confirm':
            self.confirm(message)
        else:
            print(message)






