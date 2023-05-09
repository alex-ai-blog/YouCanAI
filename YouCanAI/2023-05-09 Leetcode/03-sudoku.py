#Prompt
# Complete the following code in python3. Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules: 
#     Each of the digits 1-9 must occur exactly once in each row. 
#     Each of the digits 1-9 must occur exactly once in each column. 
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid. 
# The '.' character indicates empty cells. 
# Example 1: 
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]] 
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]] 
# Constraints: 
#     board.length == 9 
#     board[i].length == 9 
#     board[i][j] is a digit or '.'. 
#     It is guaranteed that the input board has only one solution. 
# class Solution: 
#     def solveSudoku(self, board: List[List[str]]) -> None: 
#         """ 
#         Do not return anything, modify board in-place instead. 
#         """ 

# Accepted
# Runtime: 501ms, 38.16 percentile
# Memory: 16.5MB, 11.37 percentile

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def is_valid(row: int, col: int, char: str) -> bool:
            # Check row
            for c in range(9):
                if board[row][c] == char:
                    return False
            
            # Check column
            for r in range(9):
                if board[r][col] == char:
                    return False
            
            # Check 3x3 sub-box
            box_row = (row // 3) * 3
            box_col = (col // 3) * 3
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    if board[r][c] == char:
                        return False
            
            # If all checks pass, then char is valid
            return True
        
        def backtracking() -> bool:
            # Find the next empty cell
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        # Try all possible characters in this cell
                        for char in '123456789':
                            if is_valid(r, c, char):
                                # Fill cell with valid character
                                board[r][c] = char
                                # Recurse with new board state
                                if backtracking():
                                    return True
                                # If the recursion did not find a solution, backtrack and try a new character
                                board[r][c] = '.'
                        # If no character can be placed in the cell, return False
                        return False
            # If no empty cells remain, then the puzzle has been solved
            return True
        
        backtracking()