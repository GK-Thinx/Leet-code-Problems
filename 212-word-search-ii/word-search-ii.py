class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                node = node.setdefault(ch, {})
            node['#'] = w
        res = []
        def dfs(i, j, node):
            ch = board[i][j]
            nxt = node[ch]
            if '#' in nxt:
                res.append(nxt['#'])
                del nxt['#']
            board[i][j] = '#'
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in nxt:
                    dfs(ni, nj, nxt)
            board[i][j] = ch
            if not nxt:
                del node[ch]
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return res