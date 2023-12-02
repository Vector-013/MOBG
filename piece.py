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
        self.move_list = []
        
    def move(self):
        pass
    
    def update_valid_moves(self, board):   ## re calculate valid moves of pieces
        self.move_list = self.moveSet(board)  
    
    def isSeleted(self):
        return self.selected
    
    def moveSet(self, board):   ## methods specific to each child class for calculation of valid moves
        moves = []
        return moves
    
    def change_pos(self, pos):  ## update row, col
        self.row = pos[0]
        self.col = pos[1]
    
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
    
    def moveSet(self, board):
        i = self.row
        j = self.col
        
        moves = []
        
        tr = j + 1 # for top right
        
        for q in range(i - 1, -1, -1):
            if tr < 8:
                if board[q][tr] == 0:
                    moves.append((q, tr))
                elif board[q][tr].color != self.color:
                    moves.append((q, tr))
                    break
                else:
                    break
                
            else:
                break
            
            tr += 1
            
        tl = j - 1  # top left
        
        for w in range(i - 1, -1, -1):
            if tl >= 0:
                if board[w][tl] == 0:
                    moves.append((w, tl))
                elif board[w][tl].color != self.color:
                    moves.append((w, tl))
                    break
                else:
                    break
                
            else:
                break
            
            tl -= 1
        
        bl = j - 1
        
        for w in range(i + 1, 8):
            if bl < 8 and bl >= 0:
                if board[w][bl] == 0:
                    moves.append((w, bl))
                elif board[w][bl].color != self.color:
                    moves.append((w, bl))
                    break
                else:
                    break
            else:
                break
            bl -= 1
            
        br = j + 1
        
        for w in range(i + 1, 8):
            if br < 8 and br >= 0:
                if board[w][br] == 0:
                    moves.append((w, br))
                elif board[w][br].color != self.color:
                    moves.append((w, br))
                    break
                else:
                    break
            else:
                break
            
            br += 1    
                
        return moves    

class King(Piece):
    img = 1

class Knight(Piece):
    img = 2
    def moveSet(self, board):
        i = self.row
        j = self.col
        
        moves = []
        
        try : 
            if i > 1:
                if j < 7 and (board[i - 2][j + 1] ==0 or (board[i - 2][j + 1] !=0  and  board[i - 2][j + 1].color != self.color)):
                    moves.append((i - 2, j + 1))
                    
                if j > 0 and (board[i - 2][j - 1] == 0 or (board[i - 2][j - 1] != 0 and board[i - 2][j - 1].color != self.color )):
                    moves.append((i - 2, j - 1)) 
            
            if i > 0:
                if j < 6 and (board[i - 1][j + 2] ==0 or (board[i - 1][j + 2] !=0  and  board[i - 1][j + 2].color != self.color)):
                    moves.append((i - 1, j + 2))
                
                if j > 1 and (board[i - 1][j - 2] ==0 or (board[i - 1][j - 2] !=0  and  board[i - 1][j - 2].color != self.color)):
                    moves.append((i - 1, j - 2))
                    
            if i < 6:
                if j < 7 and (board[i + 2][j + 1] ==0 or (board[i + 2][j + 1] !=0  and  board[i + 2][j + 1].color != self.color)):
                    moves.append((i + 2, j + 1))
                    
                if j > 0 and (board[i + 2][j - 1] == 0 or (board[i + 2][j - 1] != 0 and board[i + 2][j - 1].color != self.color )):
                    moves.append((i + 2, j - 1))
            
            if i < 7:
                if j < 6 and (board[i + 1][j + 2] ==0 or (board[i + 1][j + 2] !=0  and  board[i + 1][j + 2].color != self.color)):
                    moves.append((i + 1, j + 2))
                
                if j > 1 and (board[i + 1][j - 2] ==0 or (board[i + 1][j - 2] !=0  and  board[i + 1][j - 2].color != self.color)):
                    moves.append((i + 1, j - 2))      
                
        except:
            print("[ERROR] Knight moves")
        return moves

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
    def moveSet(self, board):
        i = self.row
        j = self.col
        
        moves = []
        
        for k in range(j + 1, 8):
            if board[i][k] == 0:
                moves.append((i, k))
            elif board[i][k].color != self.color:
                moves.append((i, k))
                break
            else:
                break
            
        for k in range(j - 1, -1, -1):
            if board[i][k] == 0:
                moves.append((i, k))
            elif board[i][k].color != self.color:
                moves.append((i, k))
                break
            else:
                break
        
        for k in range(i - 1, -1, -1):
            if board[k][j] == 0:
                moves.append((k, j))
            elif board[k][j].color != self.color:
                moves.append((k, j))
                break
            else:
                break
            
        for k in range(i + 1, 8):
            if board[k][j] == 0:
                moves.append((k, j))
            elif board[k][j].color != self.color:
                moves.append((k, j))
                break
            else:
                break    
      
        return moves
    