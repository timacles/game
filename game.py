import pygame 
import random 

run = True
WIDTH = 1200
HEIGHT = 700
WHITE = (155,155,255)
BLACK = (0,0,0)
VEL = 5

pygame.init()   
window = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("My Game") 

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pygame.draw.rect(window, WHITE, (self.x, self.y, self.width, self.height)) 

    def input(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0: 
            self.left()
        if keys[pygame.K_RIGHT] and self.x < WIDTH: 
            self.right()
        if keys[pygame.K_UP] and self.y > 0: 
            self.up()
        if keys[pygame.K_DOWN] and self.y < HEIGHT: 
            self.down()

    def up(self):
        self.y -= VEL
        
    def down(self):
        self.y += VEL
    
    def left(self):
        self.x -= VEL
    
    def right(self):
        self.x += VEL

class Ball(Pos):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 10
        self.height = 10

ball = Ball(50, 50)
ball2 = Ball(100, 100)
ball2.width = 5

######################################################
## MAIN LOOP
######################################################
while run:  
    pygame.time.delay(10)  
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_RSHIFT]: 
        window.fill(BLACK)       
    if keys[pygame.K_ESCAPE]: 
        run = False       

    ball.input(keys)
    ball.update()

    ball2.input(keys)
    ball2.update()


    pygame.display.update() 

pygame.quit()  
