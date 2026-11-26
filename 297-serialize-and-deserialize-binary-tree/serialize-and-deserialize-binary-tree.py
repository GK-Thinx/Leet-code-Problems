class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if node:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                vals.append('#')
        dfs(root)
        return ','.join(vals)
    def deserialize(self, data):
        if not data:
            return None
        vals = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            if vals[i] == '#':
                i += 1
                return None
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()