from p2p import BTPeer

if __name__ == "__main__":
    node0 = BTPeer(5, 8000, 'node0', "localhost")
    node1 = BTPeer(5, 8001, 'node1', "localhost")
    node2 = BTPeer(5, 8002, 'node2', "localhost")
    node3 = BTPeer(5, 8003, 'node3', "localhost")
    node4 = BTPeer(5, 8004, 'node4', "localhost")
    print(node1.numberofpeers())
    node0.addpeer('node1', "localhost", 8001)
    node0.addpeer('node2', "localhost", 8002)
    node0.addpeer('node3', "localhost", 8003)
    node0.addpeer('node4', "localhost", 8004)

    node1.addpeer('node0', "localhost", 8000)
    node1.addpeer('node2', "localhost", 8002)
    node1.addpeer('node3', "localhost", 8003)
    node1.addpeer('node4', "localhost", 8004)

    print(node1.numberofpeers())
    print(node1.connectandsend(2, "localhost", 8000, 1, 2))
    print(node2)
    node1.mainloop()
    print("node1")