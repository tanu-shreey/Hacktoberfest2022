#Tic Tac Toe, is a two player paper and pencil game

import random

class tic_tac_toe :
    def __init__(self) :
        self.board = [" " for _ in range(0, 9)]
        self.display_board()
        self.first_move = [True]

    #------------- main method----------------------------------
    def player_move(self) :
        print("\n.....Player move.....")
        try :
            move = int(input("Enter 1-9 : "))
            if self.board[move-1] == ' ' :
                self.board[move-1] = 'X'
                self.display_board()
                if self.is_winner('X') :
                    print("(^_^) Player X Wins the game!!!")
                else :
                    if self.is_board_full() :
                        print("- Game is tie!!!")
                    else :
                        if self.first_move[0]:
                            self.first_move.append(move) 
                        self.computer_move(move-1)
            else :
                print("Place is already accupied, please select another place.")
                self.player_move()
        except ValueError :
            print("Please enter valid number...")
            self.player_move()
                    
    #------------- AI based moves of computer------------------
    def computer_move(self, last_move) :
        print("\n.....Computer move.....")
        move = -1
        position_O = self.is_winning('O')
        position_X = self.is_winning('X')
        #computer can win or not in this move(attacking)
        if position_O > -1 :
            move = position_O
        #player can win or not in next move(defending)
        elif position_X > -1 :
            move = position_X
        else :
            #if first move is a corner move then we select one of the sides
            if self.first_move[0] and self.first_move[1]%2 == 1 and self.board[4] == ' ':
                move = random.choice([1, 3, 5, 7])
            #first go for center then corners and then sides
            elif self.board[4] == ' ' :
                move = 4                
            else :
                valid_corners = []
                if self.board[0] == ' ' :
                    valid_corners.append(0)
                if self.board[2] == ' ' :
                    valid_corners.append(2)
                if self.board[6] == ' ' :
                    valid_corners.append(6)
                if self.board[8] == ' ' :
                    valid_corners.append(8)

                if len(valid_corners) > 0 :
                    move = random.choice(valid_corners)
                else :
                    valid_sides = []
                    if self.board[1] == ' ' :
                        valid_sides.append(1)
                    if self.board[3] == ' ' :
                        valid_sides.append(3)
                    if self.board[5] == ' ' :
                        valid_sides.append(5)
                    if self.board[7] == ' ' :
                        valid_sides.append(7)
                    move = random.choice(valid_sides)

        self.first_move[0] = False
        self.board[move] = 'O'
        self.display_board()
        if self.is_winner('O') :
            print("[-_-] Computer Wins the game!!!")
        else :
            if self.is_board_full() :
                print("- Game is tie!!!")
            else :
                self.player_move()


    
    #------------------Helping methods-------------------------
    def display_board(self) :
        for i in range(0, 7, 3) :
            if i != 0 :
                print("  -----------------------")
            print("         |       |       ")
            print("     " + self.board[i+0] + "   |   " + self.board[i+1] + "   |   " + self.board[i+2] + " ")
            print("         |       |       ")

    def is_winner(self, p) :
        # for row positions
        for i in range(0, 7, 3) :
            if (self.board[i+0]==p and self.board[i+1]==p and self.board[i+2]==p) :
                return True
        # for column position
        for i in range(0, 3, 1) :
            if (self.board[i+0]==p and self.board[i+3]==p and self.board[i+6]==p) :
                return True        
        # for diagonal position
        if (self.board[0]==p and self.board[4]==p and self.board[8]==p) or (self.board[2]==p and self.board[4]==p and self.board[6]==p) :
            return True
        return False    

    def is_board_full(self) :
        for i in self.board :
            if i == ' ' :
                return False
        return True 

    #it returns the index of vacant place if player is winning else returns -1
    def is_winning(self, player) :
        #for all three rows
        for i in range(0, 7, 3) :
            if ((self.board[i]==player) + (self.board[i+1]==player) + (self.board[i+2]==player)) == 2 :
                for j in range(0, 3) :
                    if self.board[i+j] == ' ':
                        return (i+j)
        #for all three columns
        for i in range(0, 3) :
            if ((self.board[i]==player) + (self.board[i+3]==player) + (self.board[i+6]==player)) == 2 :
                for j in range(0, 7, 3) :
                    if self.board[i+j] == ' ':
                        return (i+j)
        #for two diagonals
        if ((self.board[0]==player) + (self.board[4]==player) + (self.board[8]==player)) == 2 :
            for i in range(0, 9, 4) :
                if self.board[i] == ' ':
                    return i
        if ((self.board[2]==player) + (self.board[4]==player) + (self.board[6]==player)) == 2 :
            for i in range(2, 7, 2) :
                if self.board[i] == ' ':
                    return i
        #if the player is not winning
        return -1
#--------------------------Driver code-------------------------------------

print("Welcome to game ----- Tic Tac Toe -----")
while True :
    new_game = tic_tac_toe()
    new_game.player_move()
    if int(input("Enter 0 to exit or 1 to play again : ")) :
        continue
    break
        
