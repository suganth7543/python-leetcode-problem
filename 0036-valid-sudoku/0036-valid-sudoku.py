class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = [[board[r][c] for r in range(9)] for c in range(9)]
        for i in range(9):
            temp=[k for k in board[i] if k!='.']
            if len(temp)!=len(set(temp)):
                return False
            temp=[k for k in columns[i] if k!='.']
            if len(temp)!=len(set(temp)):
                return False
        i=0
        temp=[]
        while(i<9):
            j=0
            while j<9:
                new=board[i][j:j+3]
                new.extend(board[i+1][j:j+3])
                new.extend(board[i+2][j:j+3])
                temp=[k for k in new if k!='.']
                if len(temp)!=len(set(temp)):
                    return False
                j=j+3
            i=i+3
        return True