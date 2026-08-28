class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def has_duplicates(arr):
            counts = {}
            for i in arr:
                if i == '.': continue
                
                if counts.get(i) is None:
                    counts[i] = 1
                else:
                    return True
            return False

        def check_arr(rows):
            for row in rows:
                if has_duplicates(row): return False
            return True
        
        columns = [[row[i] for row in board] for i in range(9)]
        boxes = []
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for k in range(3):
                    box += board[k+i][0+j:3+j]
                boxes.append(box)

        return check_arr(board) and check_arr(columns) and check_arr(boxes)