class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)
            l = dfs(node.left)
            r = dfs(node.right)
            rob = node.val + l[1] + r[1]
            not_rob = max(l) + max(r)
            return (rob, not_rob)
        return max(dfs(root))