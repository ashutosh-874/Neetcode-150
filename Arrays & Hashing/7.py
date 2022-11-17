# https://leetcode.com/problems/valid-sudoku/



'''my approach'''
# def isValidSudoku(board):


#     # row check
#     for lst in board:
#         s = set()
#         for num in lst:
#             if num != '.':
#                 if num in s:
#                     print("1")
#                     return False
#                 else:
#                     s.add(num)

#     # col check
#     for col in range(9):
#         s = set()
#         for row in range(9):
#             num = board[row][col]
#             if num != '.':
#                 if num in s:
#                     print("2")
#                     return False
#                 else:
#                     s.add(num)

#     lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
#     for i in lst:
#         for j in lst:

#             s = set()
#             for row in i:
#                 for col in j:
#                     num = board[row][col]
#                     if num != '.':
#                         if num in s:
#                             print("3")
#                             return False
#                         else:
#                             s.add(num)

#     return True


'''Neetcode's approach'''

from collections import defaultdict
def isValidSudoku(board):

    rows = defaultdict(set)
    cols = defaultdict(set)
    sqrs = defaultdict(set)



    for r in range(len(board)):
        for c in range(len(board)):
            
            num = board[r][c]
            if num != '.':

                if (num in rows[r] or 
                    num in cols[c] or 
                    num in sqrs[(r//3, c//3)]):
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                sqrs[(r//3, c//3)].add(num)

    return True








print(isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))    

