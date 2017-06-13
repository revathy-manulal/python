from random import randint
numbers = ["1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8"]
board = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
printed_board = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
solved_numbers = []
print "x denotes that that number has been solved. "" means that that number is hidden from view"
for i in printed_board:
    print i
print

def make_board():
    for a in range(4):
        for b in range(4):
            number = randint(0, (len(numbers) - 1))
            board[a][b] = numbers[number]
            del numbers[number]

def print_board():
    for i in solved_numbers:
        for a in range(4):
            for b in range(4):
                if printed_board[a][b] == i:
                    printed_board[a][b] = "x"
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
    x1 = raw_input("Enter the x coordinate of the 1st number: ")
    x1 = int(x1)
    y1 = raw_input("Enter the y coordinate of the 1st number: ")
    y1 = int(y1)
    show_input(x1, y1)
    x2 = raw_input("Enter the x coordinate of the 2nd number: ")
    x2 = int(x2)
    y2 = raw_input("Enter the y coordinate of the 2nd number: ")
    y2 = int(y2)
    show_input(x2, y2)
    if board[x1][y1] == board[x2][y2]:
        solved_numbers.append(board[x1][y1])
    print solved_numbers

def main():
    make_board()
    count = 0
    for a in range(4):
        for b in range(4):
            if printed_board[a][b] == "x":
                count += 1
    while count < 16:
        user_input()

if __name__ == "__main__":
    main()
