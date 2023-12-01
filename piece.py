import pygame
import os



b_king = pygame.image.load(os.path.join("img", "BKing.png"))
b_queen = pygame.image.load(os.path.join("img", "BQueen.png"))
b_knight = pygame.image.load(os.path.join("img", "BKnight.png"))
b_rook = pygame.image.load(os.path.join("img", "BRook.png"))
b_pawn = pygame.image.load(os.path.join("img", "BPawn.png"))
b_bishop = pygame.image.load(os.path.join("img", "BBishop.png"))

w_king = pygame.image.load(os.path.join("img", "WKing.png"))
w_queen = pygame.image.load(os.path.join("img", "WQueen.png"))
w_knight = pygame.image.load(os.path.join("img", "WKnight.png"))
w_rook = pygame.image.load(os.path.join("img", "WRook.png"))
w_pawn = pygame.image.load(os.path.join("img", "WPawn.png"))
w_bishop = pygame.image.load(os.path.join("img", "WBishop.png"))


B = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
W = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

ROW = [17.5 + 123.75*i for i in range(8)]
COL = [17.5 + 123.75*i for i in range(8)]


class Piece:
    img = -1
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        
    def move(self):
        pass
    
    def isSeleted(self):
        return self.selected
    
    def moveSet(self, board):
        moves = []
        return moves
    
    def draw(self, win, board):
        if self.color == "w":
            toDraw = W[self.img]
        else:
            toDraw = B[self.img]
            
        if self.selected:
            pygame.draw.rect(win, (255,0,0), (COL[self.col], ROW[self.row], 100,100), 5)
            
            moves = self.moveSet(board)
            
            for t in moves :
                pygame.draw.rect(win, (0,0,255), (COL[t[1]], ROW[t[0]], 100,100), 5)
            
        
        
        win.blit(toDraw, (COL[self.col], ROW[self.row]))
        
    
    
class Bishop(Piece):
    img = 0

class King(Piece):
    img = 1

class Knight(Piece):
    img = 2

class Pawn(Piece):
    img = 3
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.queen = False
        
    def moveSet(self, board):
        i = self.row
        j = self.col
        
        moves = []    # stores tuples of valid moves in (row, col)
        
        try:
            if self.color == "b":
                
                if i < 7:
                    
                    if i < 6:
                        p = board[i+1][j]
                        if p == 0:
                            moves.append((i + 1, j))
                        
                        if j < 7 and board[i + 1][j + 1] !=0 and  board[i + 1][j + 1].color != self.color:
                            moves.append((i + 1, j + 1))
                            
                        if j > 0 and board[i + 1][j - 1] !=0 and board[i + 1][j - 1] != self.color:
                            moves.append((i + 1, j - 1))
                    
                    
                    if self.first:
                        
                        if i == 1:
                            p2 = board[i+2][j]
                            if p2 == 0 and board[i + 1][j] == 0 :
                                moves.append((i + 2 ,j))
                                
                                
            else:
                if i > 0:
                    p = board[i-1][j]
                    if p == 0:
                        moves.append((i - 1, j))
                    
                    if j < 7 and board[i - 1][j+1] !=0 and board[i - 1][j + 1].color != self.color: 
                        moves.append((i - 1, j + 1))
                        
                    if j > 0 and board[i - 1][j - 1] !=0 and board[i - 1][j - 1].color != self.color:
                        moves.append((i - 1, j - 1))
                    
                    if self.first:
                        if i == 6:
                            p2 = board[i - 2][j]
                            if p2 == 0 and board[i - 1][j] == 0 :
                                moves.append((i - 2 ,j))
                        
                            
            
        except :
            print("[ERROR] : pawn moves ")
        
        return moves
        

class Queen(Piece):
    img = 4

class Rook(Piece):
    img = 5
      
    