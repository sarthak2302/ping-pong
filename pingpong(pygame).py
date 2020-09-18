import pygame
import time
pygame.init()

clock=pygame.time.Clock()

win=pygame.display.set_mode((700,500))
pygame.display.set_caption('ping.pong.pygame')

class slider():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        
    def draw(self,win):
        pygame.draw.rect(win,(255,25,0),(self.x, self.y,self.width,self.height))

class ball():
    def __init__(self,x,y,color,radius):
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
        self.velx=3
        self.vely=3
        
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)


##class gun():
##    def __init__(self,x,y,radius):
##        self.radius=radius
##        self.color=(255,255,255)
##        self.x=x
##        self.y=y
##        self.vel=3
##    def draw(self,win):
##        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)


left=slider(30,200,20,100)
right=slider(650,200,20,100)
b1=ball(345,290,(255,255,255),6)

font = pygame.font.SysFont("comicsansms", 30)
i,j=0,0
text=font.render('Player A :' + str(i) + ' Player B :' + str(j) + '',True,(255,255,0))
    
##bullets=[]
##x=0
run=True
while run:
    clock.tick(50)
    
    win.fill((0,0,0))
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run=False
     
    if b1.x<=0:
        j+=1
        text=font.render('Player A :' + str(i) + ' Player B :' + str(j) + '',True,(255,255,0))
        b1.x=350
        b1.y=250
        time.sleep(1)
        b1.velx*=-1
        b1.vely*=-1
    elif b1.x>=700:
        i+=1
        text=font.render('Player A :' + str(i) + ' Player B :' + str(j) + '',True,(255,255,0))
        b1.x=350
        b1.y=250
        time.sleep(1)
        b1.velx*=-1
        b1.vely*=-1   
        
    win.blit(text,(200,10))
    left.draw(win)
    right.draw(win)
    b1.draw(win)

##    for bullet in bullets:
##        bullet.x+=bullet.vel
##        bullet.draw(win)
##        if bullet.x>700:
##            bullets.pop(bullets.index(bullet))

    

    keys=pygame.key.get_pressed()

    if keys[pygame.K_w] and left.y>0:
        left.y-=left.vel
    elif keys[pygame.K_s] and left.y<400:
        left.y+=left.vel
    if keys[pygame.K_UP] and right.y>0:
        right.y-=right.vel
    elif keys[pygame.K_DOWN] and right.y<400:
        right.y+=right.vel

##    if keys[pygame.K_SPACE]==True and x==0:
##        if len(bullets)<=5:
##            bullets.append(gun(left.x+10,left.y+50,6))
##            x=1
##    if keys[pygame.K_SPACE]==False and x==1:
##        x=0
           

    
        
    b1.x+=b1.velx
    b1.y+=b1.vely

    if b1.y>494 or b1.y<6:
        b1.vely*=-1
    
    if ( b1.x+6==right.x and (b1.y+5>=right.y and b1.y-5<=right.y+100 )) or (b1.x-6==left.x+20 and (b1.y+5>=left.y and b1.y-5<=left.y+100)):
        b1.velx*=-1

    pygame.display.update()
