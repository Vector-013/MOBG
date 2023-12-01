from piece import *
import pygame


ROW = [17.5 + 123.75*i for i in range(8)]
COL = [17.5 + 123.75*i for i in range(8)]

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        
        self.board = [[0 for x in range(8)] for _ in range(rows)]
        
        
        
        self.board[0][0] = Rook(0, 0,"b")    ## (row, col) format, flip while reffering as (x, y) on screen
        self.board[0][1] = Knight(0 ,1, "b")
        self.board[0][2] = Bishop(0 ,2, "b")
        self.board[0][3] = Queen(0 ,3, "b")
        self.board[0][4] = King(0 ,4, "b")
        self.board[0][5] = Bishop(0 ,5, "b")
        self.board[0][6] = Knight(0 ,6, "b")
        self.board[0][7] = Rook(0 ,7, "b")
        
        self.board[1][0] = Pawn(1, 0,"b")
        self.board[1][1] = Pawn(1 ,1, "b")
        self.board[1][2] = Pawn(1 ,2, "b")
        self.board[1][3] = Pawn(1 ,3, "b")
        self.board[1][4] = Pawn(1 ,4, "b")
        self.board[1][5] = Pawn(1 ,5, "b")
        self.board[1][6] = Pawn(1 ,6, "b")
        self.board[1][7] = Pawn(1 ,7, "b")
        
        self.board[7][0] = Rook(7 , 0,"w")
        self.board[7][1] = Knight(7 ,1, "w")
        self.board[7][2] = Bishop(7 ,2, "w")
        self.board[7][3] = Queen(7 ,3, "w")
        self.board[7][4] = King(7 ,4, "w")
        self.board[7][5] = Bishop(7 ,5, "w")
        self.board[7][6] = Knight(7 ,6, "w")
        self.board[7][7] = Rook(7 ,7, "w")
        
        self.board[6][0] = Pawn(6, 0,"w")
        self.board[6][1] = Pawn(6 ,1, "w")
        self.board[6][2] = Pawn(6 ,2, "w")
        self.board[6][3] = Pawn(6 ,3, "w")
        self.board[6][4] = Pawn(6 ,4, "w")
        self.board[6][5] = Pawn(6 ,5, "w")
        self.board[6][6] = Pawn(6 ,6, "w")
        self.board[6][7] = Pawn(6 ,7, "w")
        
    def draw(self, win):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win, self.board)
                    
    def select(self, r, c):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False
        if self.board[r][c] != 0:            
            self.board[r][c].selected = True
    
    # def show_moves(self, win, r, c):
    #     if self.board[r][c] != 0 and self.board[r][c].selected:
            
            
    #         for t in self.board[r][c].moveSet(self.board) :
    #             print(t[1])
    #             try:
    #                 pygame.draw.rect(win, (0,0,255), (COL[t[1]], ROW[t[0]], 100,100), 5)
    #             except:
    #                 print("popo")
                
             
            
        
    
        