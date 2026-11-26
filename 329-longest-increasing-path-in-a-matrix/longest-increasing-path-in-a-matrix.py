import sys
sys.setrecursionlimit(1000000)
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j):
            if dp[i][j]:
                return dp[i][j]
            best=1
            val=matrix[i][j]
            for di,dj in dirs:
                ni=i+di
                nj=j+dj
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj]>val:
                    length=1+dfs(ni,nj)
                    if length>best:
                        best=length
            dp[i][j]=best
            return best
        ans=0
        for i in range(m):
            for j in range(n):
                cur=dfs(i,j)
                if cur>ans:
                    ans=cur
        return ans