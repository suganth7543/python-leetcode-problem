class Solution(object):
    def solveSudoku(self, board):
        FULL_MASK = (1 << 9) - 1  
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        def box_index(r, c):
            return (r // 3) * 3 + (c // 3)

         
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    d = int(board[r][c]) - 1
                    bit = 1 << d
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box_index(r, c)] |= bit

        def dfs():
            if not empties:
                return True

           
            best_idx = -1
            best_count = 10
            best_mask = 0
            for i, (r, c) in enumerate(empties):
                mask = FULL_MASK & ~(rows[r] | cols[c] | boxes[box_index(r, c)])
                count = bin(mask).count('1')   
                if count < best_count:
                    best_count = count
                    best_idx = i
                    best_mask = mask
                    if count == 1:
                        break

            if best_count == 0:
                return False

            r, c = empties.pop(best_idx)
            b = box_index(r, c)
            mask = best_mask

            while mask:
                bit = mask & -mask
                mask -= bit
                d = bit.bit_length() - 1
                board[r][c] = str(d + 1)

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if dfs():
                    return True

                rows[r] &= ~bit
                cols[c] &= ~bit
                boxes[b] &= ~bit
                board[r][c] = '.'

            empties.insert(best_idx, (r, c))
            return False

        dfs()
        
        
         
        