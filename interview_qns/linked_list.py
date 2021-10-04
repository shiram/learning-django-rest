class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SingleLinkedList:
    def __init__(self):
        self.headval = None

    def traverse(self):
        printval = self.headval
        list_string = ""
        while printval is not None:
            list_string += str(printval.dataval) + "->"
            printval = printval.nextval
        list_string += "(Next Node)"
        print(list_string)


    def valueExists(self, value):
        current_value = self.headval
        while current_value is not None:
            if (current_value.dataval == value) and (type(current_value.dataval) == type(value)):
                return True
            current_value = current_value.nextval
        return False

    def insertAtBegin(self, newdata):
        newNode = Node(newdata)
        newNode.nextval = self.headval
        self.headval = newNode

    def insertAtEnd(self, newdata):
        newNode = Node(newdata)
        if self.headval is None:
            self.headval  = newNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = newNode

    def insertInbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        newNode = Node(newdata)
        newNode.nextval = middle_node.nextval
        middle_node.nextval = newNode

    def removeNode(self, remove_key):
        headVal = self.headval
        if (headVal is not None):
            if (headVal.dataval == remove_key):
                self.headval = headVal.nextval
                headVal = None
                return
        while headVal is not None:
            if headVal.dataval == remove_key:
                break
            prev = headVal
            headVal = headVal.nextval

        if headVal == None:
            return
        prev.nextval = headVal.nextval
        headVal = None

list1 = SingleLinkedList()
list1.headval = Node("Mon")
e2, e3, e4 = Node("Tue"), Node("Wed"), Node("Thur")
list1.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
list1.insertAtBegin("Sun")
list1.insertAtEnd("Fri")
list1.insertInbetween(e3.nextval, "WhatDay")
list1.insertAtEnd(1)
list1.insertAtBegin(0)
list1.insertAtEnd(False)
list1.removeNode("WhatDay")
list1.traverse()
if list1.valueExists(False):
    print("Value Exists")
else:
    print("Value Does not Exist")

