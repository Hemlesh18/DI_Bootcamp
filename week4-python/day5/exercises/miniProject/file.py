# create board
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"],]

# function to print out the board
def display_board():
  for row in board:
    print(" ".join(row))
  
# prints out an empty board
display_board()

# function to handle user input and make changes to the board
def player_turn(player):
  if player == "X":
    turn = 0
  else:
    turn = 1
  
  # takes input from the user
  row = int(input("Enter row (1, 2, or 3): "))
  col = int(input("Enter column (1, 2, or 3): "))

  # checks if row or column is outside the bounds of the board
  if ((row < 1) or (col < 1)):
    print("You must enter numbers greater than 0")
  # checks if the selected square is already occupied
  elif ((board[row-1][col-1]) != "-"):
    print("Oops! That square is already taken!")
  else:
    board[row-1][col-1] = player  
    display_board()

# shuffles players in a random order
import random
turn = random.randint(0,1)

# runs until the board is full or a winner is found
check = 0
while check == 0: 
  # runs on Player X's turn
  if turn == 0:
    print("X's turn")
    player_turn("X")
    turn = 1
  # runs on Player O's turn
  else:
    print("O's turn")
    player_turn("O")
    turn = 0
  
  # checks for a win after each move
  # checks for a horizontal win 
  for row in board:
    if((row[0] == row[1]) and (row[1] == row[2]) and (row[0] != "-")):
      check = 1
      x_or_o = row[0]
      print(x_or_o + " Wins!")

  # checks for a vertical win
  if(((board[0][0] == board[1][0] )and (board[1][0] == board[2][0]) and (board[0][0] != "-") )and (check == 0)):
    check = 1
    x_or_o = board[0][0]
    print(x_or_o + " Wins!")
  # checks for a diagonal win
  elif(((board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0] != "-") )and (check == 0)):
    check = 1
    x_or_o = board[0][0]
    print(x_or_o + " Wins!")
  elif(((board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[0][2] != "-") )and (check == 0)):
    check = 1
    x_or_o = board[0][2]
    print(x_or_o + " Wins!")
  # checks for draw
  elif((board[0][0] != "-") and (board[0][1] != "-") and (board[0][2] != "-") and (board[1][0] != "-") and (board[1][1] != "-") and (board[1][2] != "-") and (board[2][0] != "-") and (board[2][1] != "-") and (board[2][2] != "-") and (check == 0)):
    check = 1
    print("Draw!")
