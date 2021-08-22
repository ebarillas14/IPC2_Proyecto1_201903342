class Node:
    def __init__(self, px, py, data):
        self.px = px
        self.py = py
        self.data = data
        self.Next = None


class LinkedList:
    def __init__(self):
        self.First = None

    def insert(self, px, py, data):
        new_node = Node(px, py, data)
        if self.First is None:
            self.First = new_node
        else:
            tmp = self.First
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = new_node
