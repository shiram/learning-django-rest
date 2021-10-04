from typing import NewType


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    
    def __init__(self):
        self.head = None

    def d_list_push(self, dataval):
        newNode = Node(dataval)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def d_list_insert(self, prev_node, newdata):
        if prev_node is None:
            return
        newNode = Node(newdata)
        newNode.next = prev_node.next
        prev_node.next = newNode
        newNode.prev = prev_node
        if newNode.next is None:
            newNode.next.prev = newNode

    def d_list_append(self, newdata):
        newNode = Node(newdata)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newNode
        newNode.prev = last
        return

    def d_list_traverse(self, node):
        while node is not None:
            print(node.data)
            node = node.next

dlist = DLinkedList()
dlist.d_list_push(1)
dlist.d_list_push(10)
dlist.d_list_push(100)
dlist.d_list_push(1000)
dlist.d_list_insert(dlist.head.next, 50)
dlist.d_list_push(50000)
dlist.d_list_insert(dlist.head.next, 150)
dlist.d_list_append(800)
dlist.d_list_append(300)
dlist.d_list_traverse(dlist.head)