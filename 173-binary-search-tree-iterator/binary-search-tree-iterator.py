class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
    def next(self):
        node = self.stack.pop()
        val = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return val
    def hasNext(self):
        return bool(self.stack)