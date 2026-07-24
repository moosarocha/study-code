# # from random import random


# # def find_best_move(board):
# #     for s in range(9):
# #         ri,ci = s//3, s%3
# #         if borad[ri][ci] == '':
# #             return ri,ci
# #         return 
    
# # def play_ttt():
# #     board = [['' for _ in range(3)] for _ in range(3)]
# #     row, col = random.randint(0, 2), random.randint(0, 2)


# # board = [['' for _ in range(3)] for _ in range(3)]
# # print(board)

# # i = input ("Enter your :")
# # ib = i.split()
# # print(ib)

# import copy
# import random
# import sys

# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("---------")
#     print()

# def is_winner(board, player):
#     # Check rows, columns, and diagonals for a win
#     for i in range(3):
#         if all(board[i][j] == player for j in range(3)) or \
#            all(board[j][i] == player for j in range(3)):
#             return True
#     if all(board[i][i] == player for i in range(3)) or \
#        all(board[i][2 - i] == player for i in range(3)):
#         return True
#     return False

# def is_full(board):
#     # Check if the board is full
#     return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# def end_game(board):
#     if is_winner(board, 'X'):
#         print("Congratulations! You won!")
#         return True
#     elif is_winner(board, 'O'):
#         print("AI 'O' wins! Better luck next time.")
#         return True
#     elif is_full(board):
#         print("It's a draw!")
#         return True
#     return False

# def get_empty_cells(board):
#     # Get the coordinates of empty cells
#     return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# # 2. ระบบ AI (Minimax Algorithm)

# def minimax(board, depth, maximizing_player):
#     if is_winner(board, 'X'):
#         return -1
#     elif is_winner(board, 'O'):
#         return 1
#     elif is_full(board):
#         return 0

#     if maximizing_player:
#         max_eval = float('-inf')
#         for i, j in get_empty_cells(board):
#             board_copy = copy.deepcopy(board)
#             board_copy[i][j] = 'O'
            
#             eval = minimax(board_copy, depth + 1, False)
#             max_eval = max(max_eval, eval)
#         return max_eval
#     else:
#         min_eval = float('inf')
#         for i, j in get_empty_cells(board):
#             board_copy = copy.deepcopy(board)
#             board_copy[i][j] = 'X'
            
#             eval = minimax(board_copy, depth + 1, True)
#             min_eval = min(min_eval, eval)
#         return min_eval

# def find_best_move(board):
#     best_val = float('-inf')
#     best_move = (-1, -1)

#     for i, j in get_empty_cells(board):
#         board_copy = copy.deepcopy(board)
#         board_copy[i][j] = 'O'
        
#         # find maximize AI turn first
#         if is_winner(board_copy, 'O'):
#             return (i, j)
            
#         move_val = minimax(board_copy, 0, False)
        
#         if move_val > best_val:
#             best_move = (i, j)
#             best_val = move_val
            
#     return best_move


# # 3. ฟังก์ชันหลักสำหรับเล่นเกม (แก้ไขบั๊กตัวเดินซ้ำแล้ว)

# def play_tic_tac_toe():
#     board = [[' ' for _ in range(3)] for _ in range(3)]
    
#     s = 0  # ใช้ตัวแปร s นับจำนวนตาเดินที่เกิดขึ้นจริง (0 ถึง 8)
    
#     while s < 9:  # Maximum of 9 moves
#         if s % 2 == 0: #สถานะเริ่มต้น
#             # ตาของผู้เล่น (X)
#             try:
#                 row, col = map(int, input("Enter your move (row space column): ").split())
#                     #ป้อนค่า
#                 # ตรวจสอบขอบเขตข้อมูลเพื่อป้องกัน IndexError
#                 if row not in range(3) or col not in range(3):
#                     print("Invalid coordinates! Please enter 0, 1, or 2.")
#                     continue
#             except ValueError:
#                 print("Invalid input! Please enter two numbers separated by space.")
#                 continue

#             if board[row][col] != ' ':
#                 print("Cell already taken. Try again.")
#                 # บั๊กถูกแก้ตรงนี้: เมื่อกรอกซ้ำ เราจะสั่ง `continue` เพื่อเริ่มลูปใหม่ 
#                 # โดยที่ไม่มีการเพิ่มค่า s ทำให้ผู้เล่นได้สิทธิ์กรอกใหม่อีกครั้ง ไม่โดนข้ามตา
#                 continue
#             else:
#                 board[row][col] = 'X'
#         else:
#             # ตาของ AI (O)
#             if s == 1:
#                 # ตาแรกของ AI ให้สุ่มเดินตามโค้ดเดิมของคุณ
#                 row, col = random.randint(0, 2), random.randint(0, 2)
#                 while board[row][col] != ' ':
#                     row, col = random.randint(0, 2), random.randint(0, 2)
#                 board[row][col] = 'O'
#             else:
#                 # ตาถัดๆ ไปใช้ Minimax หาช่องที่ดีที่สุด
#                 print("AI 'O' is thinking...")
#                 row, col = find_best_move(board)
#                 board[row][col] = 'O'
        
#         # แสดงกระดานหลังการเดินในรอบนั้นๆ
#         print_board(board)
        
#         # ตรวจสอบว่าเกมจบหรือยัง
#         if end_game(board):
#             break
            
#         s += 1  # การเดินถูกต้องเรียบร้อย ให้เพิ่มค่าตาเดินขึ้น 1

# if __name__ == "__main__":
#     play_tic_tac_toe()