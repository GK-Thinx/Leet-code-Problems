class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        res = []
        def dfs(node, path):
            if not node:
                return
            cur = path + "->" + str(node.val) if path else str(node.val)
            if not node.left and not node.right:
                res.append(cur)
            else:
                dfs(node.left, cur)
                dfs(node.right, cur)
        dfs(root, "")
        return res