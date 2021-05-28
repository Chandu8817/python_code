# board
# display a board
# play game
# handel a turn
# check wins
# check row
# check colonm
# check daigonals
# check tie
# filp palyer


# global variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

current_palyer = "X"


# game playing area
def paly_game():
    # dispaly inital board
    dispaly_board()

    while(game_still_going):
        handel_turn(current_palyer)

        check_if_game_over()

        flip_palyer()

    if winner == "X" or winner == "O":
        print(winner + "won")

    elif winner == None:
        print("tie")


#  game board function
def dispaly_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 |  2 |  3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 |  5 |  6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 |  8 |  9")


# handel palyers turns
def handel_turn(player):

    print(player, " Turns .")
    position = input("chose a position 1-9: = \n")

    vaild = False

    while not vaild:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("chose a position 1-9: = \n")
        position = int(position)-1

        if board[position] == "-":
            vaild = True
        else:
            print("you can't go there, go again ")
    board[position] = player
    dispaly_board()

# checking game is over or not


def check_if_game_over():

    check_for_win()
    check_if_tie()


# winner checking
def check_for_win():
    global winner

    # check row
    row_winners = check_rows()

    # check colonm
    col_winner = check_columns()

    # check daigonals

    dai_winner = check_daigonals()

    if row_winners:
        winner = row_winners
    elif col_winner:
        winner = col_winner

    elif dai_winner:
        winner = dai_winner

    else:
        winner = None

# checking game is tie


def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False

        return True
    else:
        return False


# change the player X to O  or O to X
def flip_palyer():

    global current_palyer

    if current_palyer == "X":
        current_palyer = "O"
    elif current_palyer == "O":

        current_palyer = "X"


# check winning rows

def check_rows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:

        game_still_going = False

    if row1:
        return board[0]

    elif row2:
        return board[3]

    elif row3:
        return board[6]
    else:
        return None

# check winning columns


def check_columns():

    global game_still_going

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:

        game_still_going = False

    if col1:
        return board[0]

    elif col2:
        return board[1]

    elif col3:
        return board[2]
    else:
        return None


# check winning daigonals

def check_daigonals():
    global game_still_going

    dal1 = board[0] == board[4] == board[8] != "-"
    dal2 = board[2] == board[4] == board[6] != "-"

    if dal1 or dal2:
        game_still_going = False

    if dal1:
        return board[0]

    elif dal2:
        return board[2]

    else:
        return None


# game is begin by calling play game function
paly_game()
