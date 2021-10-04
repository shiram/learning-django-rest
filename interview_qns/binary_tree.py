class BTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def bt_insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BTNode(data)
                else:
                    self.left.bt_insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BTNode(data)
                else:
                    self.right.bt_insert(data)
            else:
                self.data = data

    def traverse(self):
        if self.left:
            self.left.traverse()
        print(self.data)
        if self.right:
            self.right.traverse()

root = BTNode(12)
root.bt_insert(6)
root.bt_insert(14)
root.bt_insert(3)
root.bt_insert(2)
root.bt_insert(20)
root.bt_insert(5)

root.traverse()