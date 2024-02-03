board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print("0,0|0,1|0,2")
print("1,0|1,1|1,2")
print("2,0|,2,1|2,2 \n\n")
def print_board():
  for row in board:
    print("|".join(row))
    print("-" * 5)

def check_winner(player):
  for i in range(3):
    if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
      return True

  if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
    return True
  return False

def is_full():
  return all([cell != " " for row in board for cell in row])

def minimax(depth, is_maximizing):
  if check_winner("X"):
    return -1
  if check_winner("O"):
    return 1
  if is_full():
    return 0
  if is_maximizing:
    max_eval = float("-inf")
    for i in range(3):
      for j in range(3):
        if board[i][j] == " ":
          board[i][j] = "O"
          eval = minimax(depth + 1, False)
          board[i][j] = " "
          max_eval = max(max_eval, eval)
    print('max_eval:',max_eval)
    return max_eval
  else:
    min_eval = float("inf")
    for i in range(3):
      for j in range(3):
        if board[i][j] == " ":
            board[i][j] = "X"
            eval = minimax(depth + 1, True)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
    print('min_eval:',min_eval)
    return min_eval

def ai_move():
  best_move = None
  best_eval = float("-inf")
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "O"
        eval = minimax(0, False)
        board[i][j] = " "
        if eval > best_eval:
          best_eval = eval
          best_move = (i, j)
  print('best_move:',best_move)
  return best_move

while not is_full() and not check_winner("X") and not check_winner("O"):
  print_board()
  row = int(input("Enter row (0, 1, or 2): "))
  col = int(input("Enter column (0, 1, or 2): "))
  if board[row][col] == " ":
    board[row][col] = "X"
    if check_winner("X"):
      print_board()
      print("You win!")
      break
    if is_full():
      print_board()
      print("It's a draw!")
      break
    ai_row, ai_col = ai_move()
    board[ai_row][ai_col] = "O"
    if check_winner("O"):
      print_board()
      print("AI wins!")
      break

  else:
    print("Cell is already occupied. Try again.")