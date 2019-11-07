class Board(object):
    def __init__(self):
        #initializes the board
        self.cells = [" "]*9

    def display(self):
        #prints out the display
        print(self.cells[0] + '|' + self.cells[1] + '|' + self.cells[2])
        print('------')
        print(self.cells[3] + '|' + self.cells[4] + '|' + self.cells[5])
        print('------')
        print(self.cells[6] + '|' + self.cells[7] + '|' + self.cells[8])

    def update(self,cell_num,player):
        #updates the board
        if self.cells[cell_num-1] == ' ':
            self.cells[cell_num-1] = player

    def iswinner(self,player):

        #check horizontally
        if (self.cells[0] == player and self.cells[1] == player and self.cells[2] == player):
            return True
        if (self.cells[3] == player and self.cells[4] == player and self.cells[5] == player):
            return True
        if (self.cells[6] == player and self.cells[7] == player and self.cells[8] == player):
            return True

        #check vertically
        if (self.cells[0] == player and self.cells[3] == player and self.cells[6] == player):
            return True
        if (self.cells[1] == player and self.cells[4] == player and self.cells[7] == player):
            return True
        if (self.cells[2] == player and self.cells[5] == player and self.cells[8] == player):
            return True

        #check diagonal
        if (self.cells[0] == player and self.cells[4] == player and self.cells[8] == player):
            return True
        if (self.cells[6] == player and self.cells[4] == player and self.cells[2] == player):
            return True

    def reset(self):
        self.cells = [ ]*9

    def tie(self):
        used = 0
        for cell in self.cells:
            if cell != " ":
                used += 1
        if used == 9:
            return True
        else:
            return False

board = Board()

def welcome():
    print('Welcome to Tic Tac Toe\n')
    board.display()

welcome()

while True:

    # get X input
    x = int(raw_input("\n Please choose from 1-9\n (X)\n "))
    board.update(x, "X")
    board.display()

    # check if X is winner
    if (board.iswinner("X")):
        print('\n X wins !')
        replay = raw_input('Do you want to play again ? (Y/N):  ').upper()
        if (replay == "Y"):
            board.reset()
        else:
            break

    #check for tie
    if board.tie():
        print("It is a tie")
        replay = raw_input('Do you want to play again ? (Y/N):  ').upper()
        if (replay == "Y"):
            board.reset()
        else:
            break


    # get o input
    o = int(raw_input("\n Please choose from 1-9\n (O)\n "))
    board.update(o, "O")
    board.display()

    #check if Y is winner
    if (board.iswinner("Y")):
        print('\n O wins !')
        replay = raw_input('Do you want to play again ? (Y/N):  ').upper()
        if (replay == "Y"):
            board.reset()
        else:
            break

    if board.tie():
        print("It is a tie")
        replay = raw_input('Do you want to play again ? (Y/N):  ').upper()
        if (replay == "Y"):
            board.reset()
        else:
            break