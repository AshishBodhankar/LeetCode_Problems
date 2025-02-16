def exist(board: list,word:str ) -> bool:
    """
    :param board: (mxn) grid characters
    :param word: str
    :return: bool
    """
    m = len(board) # total no. of rows
    n = len(board[0]) # total no. of columns
    W = len(word) # len of the word to search in the grid

    def backtrack(pos: (int,int),index: int):
        i,j = pos

        if index == W:
            return True

        if board[i][j] != word[index]:
            return False

        char = board[i][j]
        board[i][j] = '#' # we already visited this so don't use again.

        for i_off, j_off in [(1,0),(0,1),(0,-1),(-1,0)]:
            r,c = i + i_off, j + j_off
            if 0 <= r < m and 0<= c < n:
                if backtrack((r,c),index+1):
                    return True
        board[i][j] = char
        return False

    for i in range(m):
        for j in range(n):
            if backtrack((i,j),0):
                return True

    return False