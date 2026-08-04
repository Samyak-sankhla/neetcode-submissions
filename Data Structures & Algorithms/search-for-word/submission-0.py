class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j,k):
            if len(word) == k:
                return True
            if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j] != word[k]:
                return False
            temp=board[i][j]
            board[i][j] = ''
            if backtrack(i+1,j,k+1) or backtrack(i,j+1,k+1) or backtrack(i-1,j,k+1) or backtrack(i,j-1,k+1):
                return True
            board[i][j]=temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True
        return False

            