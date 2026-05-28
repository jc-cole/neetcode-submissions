class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[c for c in row if c != "."] for row in board]
        columns = [
            [board[j][i] for j in range(9) if board[j][i] != '.'] for i in range(9)
        ]
        ranges = [
            (0, 3),
            (3, 6),
            (6, 9)
        ]

        sub_boxes = []
        for range_1 in ranges:
            for range_2 in ranges:
                sub_box = []
                for row_index in range(range_1[0], range_1[1]):
                    for column_index in range(range_2[0], range_2[1]):
                        char = board[row_index][column_index]
                        if char != '.':
                            sub_box.append(char)
                sub_boxes.append(sub_box)

        rows_valid = all(len(set(row)) == len(row) for row in rows)
        columns_valid = all(len(set(col)) == len(col) for col in columns)
        sub_boxes_valid = all(len(set(box)) == len(box) for box in sub_boxes)
        return rows_valid and columns_valid and sub_boxes_valid