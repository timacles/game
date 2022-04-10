import pygame 
import random 

imgnumint = 1

def randc():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def imgnum(imgnumint):
    imgnumint += 1
    return imgnumint


WIDTH = 1900
HEIGHT = 1000
WHITE = (155,155,255)
BLACK = (0,0,0)

pygame.init()   

window = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Drawing Design") 

x = WIDTH
y = HEIGHT

width = 5
height = 5
vel = 5
run = True





while run:  
    pygame.time.delay(10)  
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    keys = pygame.key.get_pressed() 
    
    if keys[pygame.K_LEFT] and x > 0: 
        x -= vel 
    if keys[pygame.K_RIGHT] and x < WIDTH - width: 
        x += vel 
    if keys[pygame.K_UP] and y > 0: 
        y -= vel 
    if keys[pygame.K_DOWN] and y < HEIGHT - height: 
        y += vel 
    if keys[pygame.K_RSHIFT]: 
        window.fill(BLACK)       
    if keys[pygame.K_LSHIFT]: 
        window.fill(randc()) 
    if keys[pygame.K_TAB]: 
        pygame.image.save(window, "screenshot_%s.jpeg" % (imgnum(imgnumint) - 1))        
    pygame.draw.rect(window, WHITE, (x, y, width, height)) 
    pygame.display.update() 
pygame.quit()  