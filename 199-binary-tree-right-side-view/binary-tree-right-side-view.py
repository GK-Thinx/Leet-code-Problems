class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        q = [root]
        while q:
            res.append(q[-1].val)
            nxt = []
            for node in q:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            q = nxt
        return res