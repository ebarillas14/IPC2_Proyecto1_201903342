from random import randint


class SimpleNode:
    def __init__(self, data):
        self.data = data
        self.Next = None


class SimpleLinkedList:
    def __init__(self):
        self.First = None
        self.length = 0

    def insert(self, data):
        new_node = SimpleNode(data)
        if self.First is None:
            self.First = new_node
            self.length += 1
        else:
            tmp = self.First
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = new_node
            self.length += 1

    def len(self):
        return self.length


class BasicNode:
    def __init__(self, px, py, data):
        self.px = px
        self.py = py
        self.data = data
        self.Next = None


class BasicLinkedList:
    def __init__(self):
        self.First = None
        self.length = 0

    def insert(self, px, py, data):
        new_node = BasicNode(px, py, data)
        if self.First is None:
            self.First = new_node
            self.length += 1
        else:
            tmp = self.First
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = new_node
            self.length += 1

    def get_value(self, px, py):
        tmp = self.First
        while (tmp.px != px or tmp.py != py) and tmp.Next is not None:
            tmp = tmp.Next
        return tmp.data

    def len(self):
        return self.length

    def show_all(self):
        tmp = self.First
        while tmp.Next is not None:
            print(f"en la lista de valores en la posicion x({tmp.px}) y({tmp.py}) el peso de la casilla es {tmp.data}")
            tmp = tmp.Next


class Node:
    def __init__(self, pxo, pyo, pxf, pyf, name, m, n, value_list):
        self.pxo = pxo
        self.pyo = pyo
        self.pxf = pxf
        self.pyf = pyf
        self.name = name
        self.matrix = Matrix(int(m), int(n), value_list)
        self.Next = None


class LinkedList:
    def __init__(self):
        self.First = None
        self.length = 0

    def insert(self, pxo, pyo, pxf, pyf, name, m, n, value_list):
        new_node = Node(pxo, pyo, pxf, pyf, name, m, n, value_list)
        if self.First is None:
            self.First = new_node
            self.length += 1
        else:
            tmp = self.First
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = new_node
            self.length += 1

    def get(self, name):
        tmp = self.First
        while tmp.Next is not None and tmp.name != name:
            tmp = tmp.Next
        return tmp

    def len(self):
        return self.length

    def get_all_names(self):
        tmp = self.First
        while tmp.Next is not None:
            print(tmp.name)
            tmp = tmp.Next
        print(tmp.name)

    def append(self, nodes):
        node = nodes.First
        if self.First is None:
            self.First = node
            self.length += nodes.len()
        else:
            tmp = self.First
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = node
            self.length += nodes.len()


class Matrix:
    def __init__(self, row_count, col_count, value_list):
        self.matrix = BasicLinkedList()
        self.columns = col_count
        self.rows = row_count
        rows = BasicLinkedList()
        for y in range(row_count):
            cols = BasicLinkedList()
            for x in range(col_count):
                value = value_list.get_value(x, y)
                cols.insert(x, y, value)
                # value = randint(1, 100)
                # cols.insert(x, y, value)
                # print(f" Row:{y+1} Column:{x+1} Value:{value}")
            rows.insert(0, y, cols)
        self.matrix = rows

    def get_value(self, x, y):
        row = self.matrix.get_value(0, y)
        col = row.First
        while col.px != x or col.py != y and col is not None:
            col = col.Next

        return col.data

    def display_in_menu(self):
        mt = self.matrix
        tmp = self.matrix.First
        while tmp.Next is not None:
            line = "|"
            col_tmp = tmp.data.First
            while col_tmp is not None:
                line += f"{col_tmp.data}|"
                col_tmp = col_tmp.Next
            print(line)
            tmp = tmp.Next
            """ This last part of the code is to show the last 
            iteration / last row"""
        line = "|"
        col_tmp = tmp.data.First
        while col_tmp is not None:
            line += f"{col_tmp.data}|"
            col_tmp = col_tmp.Next
        print(line)


class Stack:
    def __init__(self):
        self.First = None
        self.len = 0

    def push(self, px, py, data):
        if self.length == 0:
            self.First = BasicNode(px, py, data)
            self.len += 1
        else:
            tmp = self.First
            self.First = BasicNode(px, py, data)
            self.First.Next = tmp
            self.len += 1

    def pop(self):
        if self.len <= 0:
            print("Stack Underflow")
        else:
            tmp_res = self.First
            tmp = self.First.Next
            self.First = tmp
            self.len -= 1
            return tmp_res

    def length(self):
        return self.len

    def show_stack(self):
        tmp = self.First
        while tmp.Next is not None:
            print(f"{tmp.data}")
            tmp = tmp.Next
        print(f"{tmp.data}")

    def peek(self):
        return self.First
