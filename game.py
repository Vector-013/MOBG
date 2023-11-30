import pygame
import os
from board import Board

board = pygame.image.load(os.path.join("img", "board.png"))

width = 1000
height = 1000

ROW = []
COL = []

for i in range (8):
    ROW.append(17.5 + 123.75*i)
    COL.append(17.5 + 123.75*i)



win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")


def redraw_gameWindow():
    global win
    win.blit(board, (0,0))
    
    play_board = Board(8, 8)
    play_board.draw(win)
    
    pygame.display.update()

def click(pos):
    """
    return pos (x,y) of click in range 0-7 0-7
    """
    x = pos[0]
    y = pos[1]
    
    for i in range(8):
        for j in range(8):
            if x>=COL[i]-17.5 and x<=COL[i]+106.25 and y>=ROW[j]-17.5 and y<=ROW[j]+106.25:
                print(i ,j)
                return i, j   
    
def main():
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(10)
        redraw_gameWindow()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                break
                
            if event.type == pygame.MOUSEMOTION:
                pass
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                r,c = click(pos)
            



main()