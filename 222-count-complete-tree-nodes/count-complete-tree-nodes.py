class Solution:
    def countNodes(self, root):
        def depth_left(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d
        def depth_right(node):
            d = 0
            while node:
                d += 1
                node = node.right
            return d
        if not root:
            return 0
        dl = depth_left(root)
        dr = depth_right(root)
        if dl == dr:
            return (1 << dl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)