# SCP_matbogi
Matbogi project for BOSCoin - prototyping SCP 


## Dependencies
```
python3
```

## Assumptions
* Federated voting process
* Instead of a p2p model, this implementation is a client-server model where the server broadcasts 
all the client's messages to the other clients.
* Assume that the server is not corrupt and the connection between the clients are secure
* A quorum consists of five nodes, and the threshold is set to 4
* There are no faulty nodes
* All messages are considered valid
* Messages are encoded in json format, for example:
```json
{'nodeID': nodeID, 'msgType': vote}
```

## Running

To start the main server

`python server.py`

in another terminal,

`python client.py`

for each node 

Set the node name for each node, and send `start` in one of the clients to start voting

## TODOs

* Implement blocking threshold
* Set a node as faulty
* Dynamic quorum construction
* Hashing 
* Validating the messages
* Instead of a client-server architecture, use p2p
* Record the history of a node's fields in msg_list


## References

* [Let's Write a Chat App in Python](https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170)
* [Stellar Consensus Protocol - IETF draft](https://tools.ietf.org/html/draft-mazieres-dinrg-scp-01)