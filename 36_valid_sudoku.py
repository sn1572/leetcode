class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = []
        rows = []
        subs = []
        for i in range(9):
            cols.append({})
            rows.append({})
            subs.append({})
        col_dict = dict(zip(range(9), cols))
        row_dict =  dict(zip(range(9), rows))
        sub_dict = dict(zip(range(9), subs))
        for i in range(9):
            row = row_dict[i]
            for j in range(9):
                col = col_dict[j]
                num = board[i][j]
                if num == '.':
                    pass
                else:
                    if num in col:
                        return(False)
                    else:
                        col[num] = 1
                    if num in row:
                        return(False)
                    else:
                        row[num] = 1
                    sub = sub_dict[3*int(i/3)+int(j/3)]
                    if num in sub:
                        return(False)
                    else:
                        sub[num] = 1
        return(True)