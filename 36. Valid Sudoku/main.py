from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row: int) -> bool:
            s = set()
            for d in board[row]:
                if d != ".":
                    if d in s:
                        return False
                    s.add(d)

            return True

        def checkCol(col: int) -> bool:
            s = set()
            for row in board:
                d = row[col]
                if d != ".":
                    if d in s:
                        return False
                    s.add(d)

            return True

        def checkSubBox(top: int, left: int) -> bool:
            s = set()

            for row in range(top * 3, (top + 1) * 3):
                for col in range(left * 3, (left + 1) * 3):
                    d = board[row][col]
                    if d != ".":
                        if d in s:
                            return False
                        s.add(d)

            return True

        for i in range(9):
            if not checkRow(i):
                return False
            if not checkCol(i):
                return False

        for top in range(3):
            for left in range(3):
                if not checkSubBox(top, left):
                    return False

        return True


def main():
    print(Solution().isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))


if __name__ == "__main__":
    main()
