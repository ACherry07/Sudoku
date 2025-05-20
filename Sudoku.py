from glob import glob
from importlib.machinery import BYTECODE_SUFFIXES
import pygame
from random import *
import time
from os import system, name
from time import sleep

#start of nos
start = time.time()
l = [1,2,3,4,5,6,7,8,9]
bah = ['']*9
s = [bah]*9
sc = s.copy()
row = 0
st = time.time()
while bah in s:
    shuffle(l)
    n = 0
    k = l.copy()

    for i in range(len(k)):
        r = row//3*3
        c = i//3*3
        box = [s[r][c], s[r][c+1], s[r][c+2], s[r+1][c],  s[r+1][c+1], s[r+1][c+2], s[r+2][c], s[r+2][c+1], s[r+2][c+2]]
        for j in s:
            if k[i]  == j[i]:
                n = 1
            elif k[i] in box:
                n = 1    
        if n == 1:
            break
        if time.time() - st > 4.0:
            st = time.time()
            s = sc.copy()
            row = 0
            break
            
    else:
        s[row] = k
        row += 1
        st = time.time()

#print(time.time()-start)


level = int(input("Choose level\n1.EASY\n2.MEDIUM\n3.HARD\nChoice (1,2,3):"))
if level == 1:
    total = randint(27,32)
elif level == 2:
    total = randint(38,42)
elif level == 3:
    total = randint(48,51)
s2 = []
for i in s:
    ii = i.copy()
    s2.append(ii)

tot = 0

while tot < total:
    r11 = choice([1,2,3,4,5,6,7,8,9])-1
    c11 = choice([1,2,3,4,5,6,7,8,9])-1
    if s2[r11][c11] != '':
        s2[r11][c11] = ''
        tot += 1

s2o = []
for i in s2:
    ii = i.copy()
    s2o.append(ii)  
#end of nos



color_active = (0,0,255)
color_passive = (100,100,100)
color = color_passive
boxes = []
texts = ['']*81
textsorg = ['']*81
textstot = ['']*81
var = 99
old = ''
print("Hi there! Let's Play a game.")
l = [int(input("Enter width of window (>600):"))]
l.append(l[0]*4/5)

#adding nos to list
for nos in range(9):
    for nos1 in range(9):
        textstot[9*nos+nos1] = str(s[nos][nos1])
for nos in range(9):
    for nos1 in range(9):
        if s2[nos][nos1] != '':
            texts[9*nos+nos1] = str(s2[nos][nos1])
            textsorg[9*nos+nos1]= str(s2[nos][nos1])
        else:
            texts[9*nos+nos1] = s2[nos][nos1]
            textsorg[9*nos+nos1] = s2[nos][nos1]


#Initialize pygame
pygame.init()

#Title and Icon
pygame.display.set_caption('Sudoku')
icon = pygame.image.load(r'D:\Python Stuff\Python VSCODE\Pygame\Icons\sudoku.png')
pygame.display.set_icon(icon)


#Screen
screen = pygame.display.set_mode(l)

#Font
base_font = pygame.font.SysFont("PalatinoLinotype", 22)
user_text = ''


#GRID

def grid():
    global boxes
    global var
    global texts
    global old
    s = 45
    k = 9*s
    startx = l[0]//2 - eval('k/2')
    starty = l[1]//2 - eval('k/2')
    corners = [(startx,starty),(startx+k,starty),(startx+k,starty+k),(startx,starty+k)]
    grid1 = pygame.Rect(startx,starty,k,k)
    x1 = starty - 45
    for j in range(9):
        x1 += 45
        x2 = startx - 45
        for j in range(9):
            x2 += 45
            box = pygame.Rect(x2,x1,45,45)
            boxes.append(box)
    for j in boxes:
        pygame.draw.rect(screen,color_passive,j,1)
        b2 = texts[boxes.index(j)]
        if b2 == textsorg[boxes.index(j)]:
            text_surface = base_font.render(b2,True,(0,0,0))
            screen.blit(text_surface,(j.x + 16, j.y + 10))
        else:
            text_surface = base_font.render(b2,True,(200,0,0))
            screen.blit(text_surface,(j.x + 16, j.y + 10))
        
    pygame.draw.rect(screen,(0,0,0),grid1,5)
    x1 = startx
    x2 = starty
    for i in range(1,3):

        linesx = pygame.draw.line(screen,(0,0,0),(x1,x2+3*i*45),(x1 + k - 5,x2+3*i*45),3)
        linesx = pygame.draw.line(screen,(0,0,0),(x1+3*i*45,x2),(x1 + 3*i*45,x2+k-5),3)
    for j in boxes:
        if boxes.index(j) == var:
            pygame.draw.rect(screen,color_active,j,3)
            b2 = texts[var]
            if b2 == '' and old != '':
            #print(b2)
                text_surface = base_font.render(old,True,(200,0,0))
                screen.blit(text_surface,(j.x + 16, j.y + 10))
                old = old
            else:
                text_surface = base_font.render(b2,True,(200,0,0))
                screen.blit(text_surface,(j.x + 16, j.y + 10))
                old = ''
                

def text_objects(text,font):
    textSurface = font.render(text,True,(0,105,255))
    return textSurface, textSurface.get_rect()

def message_display(text):
    s = 45
    k = 9*s
    startx = l[0]//2 - eval('k/2')
    starty = l[1]//2 - eval('k/2')
    largetext = pygame.font.SysFont("CourierNew",60)
    textsurf, textrect = text_objects(text,largetext)
    textrect.center = (l[0]/2,starty-40)
    if text == "YOU WIN":
        textrect.center = (l[0]/2,l[1]/2)
    screen.blit(textsurf,textrect)

def head(text):
    message_display(text)



#Game Loop
active = False
run = True
i = 1
while run:
    if texts == textstot:
        sleep(3)
        break

    screen.fill((255,255,150))
    head("SUDOKU")
    k = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            for i in range(len(boxes)):

                if boxes[i].collidepoint(event.pos):
                    active = True
                    var = i
                    old = texts[i]
                    break
            else:
                active = False
                var = 99
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if var%9 != 0:
                    var -= 1
                    i = var
                    active = True
                    old = texts[i]
            if event.key == pygame.K_RIGHT:
                if var%9 != 8:
                    var += 1
                    i = var
                    active = True
                    old = texts[i]
            if event.key == pygame.K_UP:
                if var>8:
                    var -= 9
                    i = var
                    active = True
                    old = texts[i]
            if event.key == pygame.K_DOWN:
                if var < 72:
                    var += 9
                    i = var
                    active = True 
                    old = texts[i]       
            if event.key == pygame.K_ESCAPE:
                run = False
            if active == True and textsorg[i]== '':
                if len(texts[i]) != 0 :
                    if event.key == pygame.K_BACKSPACE:
                        texts[i] = user_text[:-1]
                    else:
                        if event.unicode in "123456789":
                            texts[i] = event.unicode
                        if event.unicode == '':
                            texts[i] = old
                        
                else:
                    if event.unicode in "123456789":
                        texts[i] += event.unicode

    '''if active:
        b1 = boxes[i]
        text_surface = base_font.render(texts[i],True,(100,100,100))
        screen.blit(text_surface,(b1.x + 16, b1.y + 10))'''
    
    grid()

    if texts == textstot:
        screen.fill((255,255,150))
        head("YOU WIN")
    pygame.display.update()