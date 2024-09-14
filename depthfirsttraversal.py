class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root != None:
            cur = self.root
            while cur != None:
                if data < cur.data:
                    if cur.left != None:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break
                elif data > cur.data:
                    if cur.right != None:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        break
        else:
            self.root = Node(data)
    def in_order_traversal_r(self, node, buffer):
        cur = node
        if cur != None:
            self.in_order_traversal_r(cur.left, buffer)
            buffer.append(cur.data)
            self.in_order_traversal_r(cur.right, buffer)
        else:
            return None
    def in_order_traversal(self):
        buffer = []
        self.in_order_traversal_r(self.root, buffer)
        return buffer
    def pre_order_traversal_r(self, node, buffer):
        cur = node
        if cur != None:
            buffer.append(cur.data)
            self.pre_order_traversal_r(cur.left, buffer)
            self.pre_order_traversal_r(cur.right, buffer)
        else:
            return None
    def pre_order_traversal(self):
        buffer = []
        self.pre_order_traversal_r(self.root, buffer)
        return buffer
    def post_order_traversal_r(self, node, buffer):
        cur = node
        if cur != None:
            self.post_order_traversal_r(cur.left, buffer)
            self.post_order_traversal_r(cur.right, buffer)
            buffer.append(cur.data)
        else:
            return None
    def post_order_traversal(self):
        buffer = []
        self.post_order_traversal_r(self.root, buffer)
        return buffer

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)
bst.insert(4)
bst.insert(6)
in_order = bst.in_order_traversal()
pre_order = bst.pre_order_traversal()
post_order = bst.post_order_traversal()
print(in_order)
print(pre_order)
print(post_order)

