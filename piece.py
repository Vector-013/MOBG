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

ROW = []
COL = []

for i in range (8):
    ROW.append(17.5 + 123.75*i)
    COL.append(17.5 + 123.75*i)

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
    
    def draw(self, win):
        if self.color == "w":
            toDraw = W[self.img]
        else:
            toDraw = B[self.img]
        
        win.blit(toDraw, (COL[self.col], ROW[self.row]))
        
    
    
class Bishop(Piece):
    img = 0

class King(Piece):
    img = 1

class Knight(Piece):
    img = 2

class Pawn(Piece):
    img = 3

class Queen(Piece):
    img = 4

class Rook(Piece):
    img = 5
      
    