import pygame

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
        