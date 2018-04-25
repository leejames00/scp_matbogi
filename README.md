# scp_matbogi
Matbogi project for BOSCoin - prototyping SCP 


## Dependencies
```
python3
```

## Assumptions
* instead of a p2p model, this implementation is a client-server model where the server broadcasts 
all the client's messages to the other clients.
* assume that the server is not corrupt and the connection between the clients are secure
* A quorum consists of five nodes
* There are no faulty nodes
* all messages are considered valid
* messages are encoded in json format, for example:
```json
{'nodeID': nodeID, 'msgType': vote}
```

## Implementation

## TODOs
voted 으로 넣을때 node별로 넣어야함.
voted = {'vote(a)': [node0, node1, node2, node3]} 이런식으로
mylist = list(set(mylist)) --> 이러면 node 중복 없이 store 가능.

## References

* [Let's Write a Chat App in Python](https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170)
* [Stellar Consensus Protocol - IETF draft](https://tools.ietf.org/html/draft-mazieres-dinrg-scp-01)