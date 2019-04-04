from random import randint
import operator

board = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]

def print_board():
    for x in board:
        print x
    print "\n"

def user_input():
    userX = raw_input("In which row would you like to play? ")
    userX = int(userX)
    userY = raw_input("In which column would you like to play? ")
    userY = int(userY)
    if board[userX][userY] == "0":
        board[userX][userY] = "2"
    else:
        print "You entered invalid coordinates. Try again."
		user_input()
    print_board()

def play_move(x, y, win=False):
    board[x][y] = "1"
    print "my move:"
    print_board()
    counter = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] != "0":
                counter += 1
    if counter == 9:
        return False
    if not win:
        user_input()
    return True

def is_user_start():
    Str = randint(0, 1)
    if Str == 1:
        Str = True
        return Str
    else:
        Str = False
        return Str

def defense():
    #defend rows
    for x in range(3):
        if board[x] == ["2", "2", "0"]:
            play_move(x, 2)
            return True
        elif board[x] == ["2", "0", "2"]:
            play_move(x, 1)
            return True
        elif board[x] == ["0", "2", "2"]:
            play_move(x, 0)
            return True
    count = 0
    count2 = 0
    #defend columns
    for y in range(3):
        column = get_column(y)
        for i in range(len(column)):
            if column[i] == "2":
                count += 1
            if column[i] == "0":
                count2 += 1
        if count == 2 and count2 == 1:
            for i in range(len(column)):
                if column[i] == "0":
                    play_move(i, y)
        #Defend diagonal
        count = 0
        count2 = 0
    for x in range(3):
        y = x
        if board[x][y] == "2":
            count += 1
        if board[x][y] == "0":
            count2 += 1
    if count == 2 and count2 == 1:
        for x in range(3):
            y = x
            if board[x][y] == "0":
                play_move(x, y)
                return True
    #defend reverse diagonal
    count = 0
    count2 = 0
    y = 2
    for x in range(3):
        if board[x][y] == "2":
            count += 1
        if board[x][y] == "0":
            count2 += 1
        y -= 1
    if count == 2 and count2 == 1:
        y = 2
        for x in range(3):
            if board[x][y] == "0":
                play_move(x, y)
                return True
            y -= 1
    return False

def play_winning_move():
    #win in a row
    for x in range(3):
          if board[x] == ["1", "1", "0"]:
              play_move(x, 2, True)
              print "I WON!!!!!!!!!"
              return True
          elif board[x] == ["1", "0", "1"]:
              play_move(x, 1, True)
              print "I WON!!!!!!!!!"
              return True
          elif board[x] == ["0", "1", "1"]:
              play_move(x, 0, True)
              print "I WON!!!!!!!!!"
              return True
              #win in a column
    count = 0
    count2 = 0
    for y in range(3):
        column = get_column(y)
        for i in range(len(column)):
            if column[i] == "1":
                count += 1
            if column[i] == "0":
                count2 += 1
        if count == 2 and count2 == 1:
            for i in range(3):
                if column[i] == "0":
                    play_move(i, y)
                    print "I WON!!!!!!!!!"
                    return True
    count = 0
    count2 = 0
    #win in diagonal
    for x in range(3):
        y = x
        if board[x][y] == "1":
            count += 1
        if board[x][y] == "0":
            count2  += 1
        if count == 2 and count2 == 1:
            for x in range(3):
                y = x
                if board[x][y] == "0":
                    play_move(x, y, True)
                    print "I WON!!!!!!!!!"
                    return True
        #win in reverse diagonal
        count = 0
        count2 = 0
        y = 2
    for x in range(3):
        if board[x][y] == "1":
            count += 1
        if board[x][y] == "0":
            count2 += 1
        y -= 1
    y = 2
    if count == 2 and count2 == 1:
        for x in range(3):
            if board[x][y] == "0":
                play_move(x, y, True)
                print "I WON!!!!!!!!!"
                return True
            y -= 1
    return False

def get_column(y):
    column_values = []
    for x in range(3):
        column_values.append(board[x][y])
    return column_values

def get_diagonal():
    diagonal_values = []
    for x in range(3):
        y = x
        diagonal_values.append(board[x][y])
    return diagonal_values

def get_backdiagonal():
    backdiagonal_values = []
    x = 2
    for y in range(3):
        backdiagonal_values.append(board[x][y])
        x -= 1
    return backdiagonal_values

def is_in_diagonal(x, y):
    return x == y
def is_in_backdiagonal(x, y):
    return (x == 0 and y == 2) or (x == 1 and y == 1) or (x == 2 and y == 0)

def move_evaluation():
    win_combo_array = {}
    win_combos = 0
    counter = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] != "0":
                continue
            #row evaluation
            for m in board[x]:
                if m != "2":
                    continue
                else:
                    counter += 1
            if counter == 0:
                win_combos += 1
            counter = 0
            #column evaluation
            column = get_column(y)
            for l in column:
                if l != "2":
                    continue
                else:
                    counter += 1
            if counter == 0:
                win_combos += 1
            counter = 0
            #diagonal evaluation
            if is_in_diagonal(x, y):
                diagonal = get_diagonal()
                for l in diagonal:
                    if l != "2":
                        continue
                    else:
                        counter += 1
                if counter == 0:
                    win_combos += 1
            counter = 0
            #reverse diagonal evaluation
            if is_in_backdiagonal(x, y):
                backdiagonal = get_backdiagonal()
                for l in backdiagonal:
                    if l != "2":
                        continue
                    else:
                        counter += 1
                if counter == 0:
                    win_combos += 1
            win_combo_array[(x, y)] = win_combos
            win_combos = 0
    try:
        sortedw = sorted(win_combo_array.items(), key = operator.itemgetter(1))
        x, y = sortedw[-1][0]
        return play_move(x, y)
    except IndexError:
        return False

def main():
    print_board()
    if is_user_start():
        print "You are starting."
        user_input()
    if not is_user_start():
        print "I am starting"
    while True:
        count = 0
        if board[1][1] == "1":
            for x in range(3):
                if board[x][x] == "2":
                    count += 1
            if count == 2:
                play_move(1, 0)
            b = 0
            count = 0
            for a in range(3):
                if board[a][b] == "2":
                    count += 1
                b -= 1
            if count == 2:
                play_move(1, 0)
        if play_winning_move():
            return
        if not defense():
            notfin = move_evaluation()
            if not notfin:
                print "TIE :|"
                return

if __name__ == "__main__":
    main()
