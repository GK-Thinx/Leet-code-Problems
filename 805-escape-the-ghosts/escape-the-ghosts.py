class Solution:
    def escapeGhosts(self, ghosts, target):
        my = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            if abs(x - target[0]) + abs(y - target[1]) <= my:
                return False
        return True