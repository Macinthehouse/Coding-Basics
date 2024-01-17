import pygame
from pathlib import Path
import time
# 77, 20, 40
#color pallete
black = (0, 0, 0)
orange = (152, 72, 51)
white = (255, 255, 255)

#opening the text file in read mode
cre_fl = open(Path.home() / 'end_credits.txt', 'r+')

#initializing pygame window
pygame.init()
w = 800 #width
h = 500 #height
#setting the window dimensions
window = pygame.display.set_mode((w,h)) 
#setting the pygame window name
pygame.display.set_caption('End Credit')
#anouncing the window as a rectangle
window_rect = window.get_rect()
#setting the font and font size for the text
font = pygame.font.SysFont(pygame.font.get_fonts()[178], 22) #pulling the font out of the inbuilt pygame get.fonts() function
#filling the background with black                257 178
window.fill(orange)
clock = pygame.time.Clock()

def gag_r(w, h, window):
    w = (w // 4) - 140
    h = (h // 2) - 140
    gags = ['gag_1.png', 'gag_2.png', 'gag_3.png', 'gag_4.png', 'gag_5.png']
    
    for i in gags:
        gag = pygame.image.load(i)
        window.blit(gag, (w,h))
        pygame.display.update()
        time.sleep(1)
    
def main():         
    #position counter
    a = 0
    #addition counter
    b = 0
    #position at which new line add in
    c = 30
    #creating a list of all the lines present in the external file
    lines = cre_fl.readlines()
    text = [] 
    
    #iterating the list (lines) to replace '\n' with '', and create a new list 
    for i in lines:
        new = i.split('\n')
        #iterating each index of lines since it is a multidimensional list
        for j in new: 
            if j != '':
                text.append(j) #new list containing the lines in external file
   
    ind_pos = []
    ind_pos.append('') #adding a empty index so when the list appends starting position of lines while itereating the position index will match text index.
    add = []
    add.append('') #adding a empty index so when the list appends the addition value of each line while itereating the position index will match text index.
    t_pos = []
    
    ate = ((h // len(text)) + (h + (h // 4)))
    for num in range(ate):
        count = -1
        for line in text:
            count += 1
            if (num == 0) and (line != text[0]):
                #renders the first line of the external file
                t = font.render(line, True, white, orange)
                #creates a rectangle around the text
                rect = t.get_rect()
                #setting the ceter position of the rectangle
                rect.center = (w - 270, h + c)
                #starting postion for all lines in text except line in text[0]
                ind_pos.append((h + c))
                #addition value of each line in text except line in text[0]
                add.append(b)
                #appending the text and its position into new list
                t_pos.append((t, rect))
                c += 30
            
            elif (num > 0) and (line != text[0]):
                #adding 1 to the addition value according to the line index
                b = (add[count] + 1)
                #changing the addition value according to the line index
                add.insert(count, b)
                #height value according to the line index
                c = ind_pos[count]
                #renders the first line of the external file
                t = font.render(line, True, white, orange)
                #creates a rectangle around the text
                rect = t.get_rect()
                #setting the ceter position of the rectangle
                rect.center = (w - 270, c - b)
                #appending the text and its position into new list
                t_pos.append((t, rect))
            
            elif line == text[0]:
                #renders the first line of the external file
                t = font.render(line, True, white, orange)
                #creates a rectangle around the text
                rect = t.get_rect()
                #setting the ceter position of the rectangle
                r = rect.center = (w - 270, h - a)
                #appending the text and its position into new list
                t_pos.append((t, rect))
                a += 1
    
    while True:
        #iterating the list containing t and r to create scrolling
        for t, rect in t_pos:    
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    return()
                
            #blitting the text with rectangle 
            window.blit(t, rect)  
            #frames per second
            clock.tick(80)
            #updating the display to show text
            pygame.display.update()
        
        gag_r(w, h, window)
        
        #end loop when text crosses the pygame window
        if not window_rect.collidelistall([rect for (rect, _) in t_pos]):
            return
        
        pygame.display.flip()
            
main()
        


