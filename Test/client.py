import pygame
from network import Network

swidth = 500
sheight = 500
win = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self):    
            self.rect = (self.x, self.y, self.width, self.height)
        
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            
        if keys[pygame.K_UP]:
            self.y -= self.vel
            
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        
        self.update()
        #if self.x >=0 and self.x <=swidth-self.width and self.y >=0 and self.y <=sheight-self.height:
            #print(self.x ," ", self.y)
        
        

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1]) 

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])       

def redrawWindow(player, win, player2):
    win.fill((0, 0, 0))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()
    

def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (255,0,0))
    p2 = Player(0, 0,100,100,(255,0,0))
    clock = pygame.time.Clock()
    
    
    while run:
        clock.tick(60)
        
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p.move()        
        redrawWindow(p, win, p2)
        

main()