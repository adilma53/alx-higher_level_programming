#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
            return
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        head_copy = self.__head
        while head_copy and head_copy.next_node and head_copy.next_node.data < value:
            head_copy = head_copy.next_node

        new_node.next_node = head_copy.next_node
        head_copy.next_node = new_node
        return

    def __str__(self):
        value = []
        tmp = self.__head
        while tmp is not None:
            value.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(value))
