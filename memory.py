from random import randint
numbers = ["1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8"]
board = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
printed_board = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
solved_numbers = []
print "Welcome to memory game!"
print "x denotes that that number has been solved. %r means that that number is hidden from view" % ""

def make_board():
    for a in range(4):
        for b in range(4):
            number = randint(0, (len(numbers) - 1))
            board[a][b] = numbers[number]
            del numbers[number]

def print_board():
    print solved_numbers
    for a in range(4):
        for b in range(4):
            if board[a][b] in solved_numbers:
                printed_board[a][b] = board[a][b]
    for i in printed_board:
        print i
    print

def show_input(x, y):
    printed_board[x][y] = board[x][y]
    for i in printed_board:
        print i
    for a in range(4):
        for b in range(4):
            printed_board[a][b] = ""
    for i in solved_numbers:
        for a in range(4):
            for b in range(4):
                if board[a][b] == i:
                    printed_board[a][b] == "x"

def user_input():
    x1, y1 = take_valid_input1()
    show_input(x1, y1)
    x2, y2 = take_valid_input2(x1, y1)
    show_input(x2, y2)
    if board[x1][y1] == board[x2][y2]:
        solved_numbers.append(board[x1][y1])
    print_board()

def take_valid_input1():
    while True:
        x1 = int(raw_input("Enter the x coordinate of the 1st number: "))
        y1 = int(raw_input("Enter the y coordinate of the 1st number: "))
        if printed_board[x1][y1] == "":
            return x1, y1

def take_valid_input2(x1, y1):
    coordinate1 = x1, y1
    while True:
        x2 = int(raw_input("Enter the x coordinate of the 2nd number: "))
        y2 = int(raw_input("Enter the y coordinate of the 2nd number: "))
        coordinate2 = x2, y2
        if printed_board[x1][y1] == "" and coordinate1 != coordinate2:
            return x2, y2

def main():
    make_board()
    while len(solved_numbers) < 8:
        user_input()
    print "YOU WIN!!!"

main()
