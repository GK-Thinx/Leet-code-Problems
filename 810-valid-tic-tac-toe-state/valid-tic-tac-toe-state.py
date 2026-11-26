class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        x = sum(row.count('X') for row in board)
        o = sum(row.count('O') for row in board)
        if o > x or x - o > 1:
            return False
        lines = []
        for i in range(3):
            lines.append([board[i][0], board[i][1], board[i][2]])
            lines.append([board[0][i], board[1][i], board[2][i]])
        lines.append([board[0][0], board[1][1], board[2][2]])
        lines.append([board[0][2], board[1][1], board[2][0]])
        x_win = any(all(c == 'X' for c in line) for line in lines)
        o_win = any(all(c == 'O' for c in line) for line in lines)
        if x_win and o_win:
            return False
        if x_win and x != o + 1:
            return False
        if o_win and x != o:
            return False
        return True