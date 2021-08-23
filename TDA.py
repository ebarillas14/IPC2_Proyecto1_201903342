from random import randint


class BasicNode:
    def __init__(self, px, py, data):
        self.px = px
        self.py = py
        self.data = data
        self.Next = None


class BasicLinkedList:
    def __init__(self):
        self.First = None

    def insert(self, px, py, data):
        new_node = BasicNode(px, py, data)
        if self.First is None:
            self.First = new_node
        else:
            tmp = self.First
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = new_node

    def get_value(self, px, py):
        tmp = self.First
        while tmp.px != px or tmp.py != py:
            tmp = tmp.Next
        return tmp


class Node:
    def __init__(self, pxo, pyo, pxf, pyf, name):
        self.pxo = pxo
        self.pyo = pyo
        self.pxf = pxf
        self.pyf = pyf
        self.name = name
        self.Next = None


class LinkedList:
    def __init__(self):
        self.First = None

    def insert(self, pxo, pyo, pxf, pyf, name):
        new_node = Node(pxo, pyo, pxf, pyf, name)
        if self.First is None:
            self.First = new_node
        else:
            tmp = self.First
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = new_node


class Matrix:
    def __init__(self, row_count, col_count):
        self.matrix = BasicLinkedList()
        self.columns = col_count
        self.rows = row_count
        rows = BasicLinkedList()
        for y in range(row_count):
            cols = BasicLinkedList()
            for x in range(col_count):
                value = randint(1, 100)
                cols.insert(x, y, value)
                print(f" Row:{y+1} Column:{x+1} Value:{value}")
            rows.insert(0, y, cols)
        self.matrix = rows

    def get_value(self, row, col):
        rows = self.matrix.get_value(0, row)
        cols = rows.data
        item = cols.get_value(col, row)
        return item.data
    
    def display_in_menu(self):
        tmp = self.matrix.First
        while tmp.Next is not None:
            line = "|"
            col_tmp = tmp.data.First
            while col_tmp is not None:
                line += f"{col_tmp.data}|"
                col_tmp = col_tmp.Next
            print(line)
            tmp = tmp.Next
        line = "|"
        col_tmp = tmp.data.First
        while col_tmp is not None:
            line += f"{col_tmp.data}|"
            col_tmp = col_tmp.Next
        print(line)
        return
