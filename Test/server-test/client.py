import pygame
from network import Network
import pickle
from player import Player

swidth = 500
sheight = 500
win = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("Client")

        
def redrawWindow(player, win, player2):
    win.fill((0, 0, 0))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()
    

def main():
    run = True
    n = Network()
    clock = pygame.time.Clock()
    p = n.getP()
    
    while run:
        clock.tick(60)
        p2 = n.send(p)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p.move()        
        redrawWindow(p, win, p2)
        

main()