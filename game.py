import pygame
import os
from piece import *

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
    
    bishop = Bishop(3,6,"b")
    bishop.draw(win)
    pygame.display.update()
    
    
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
                pass
            



main()