import pygame
import time
import random

pygame.init()

displayInfo = pygame.display.Info()
display_width = displayInfo.current_w
display_height = displayInfo.current_h

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
gameDisplay.fill(white)

# Reference width and height for font size 450
ref_w, ref_h = 1366, 768 
# Current display width and height
cur_w, cur_h = display_width, display_height

'''
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
''' 

def text_objects(text, font):
    textSurface = font.render(text, True, black).convert_alpha()
    txt_w, txt_h = textSurface.get_size()
    textSurface = pygame.transform.smoothscale(textSurface, (txt_w * cur_w // ref_w, txt_h * cur_h // ref_h))
    return textSurface, textSurface.get_rect()  
	
def message_display(text):
    largeText = pygame.font.Font('digifaw.ttf',450)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(1)
	
def display():
    counter = 0
    running  = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        message_display(str(counter))
        gameDisplay.fill(white)
        counter = counter + 1
			
display()				
pygame.quit()
quit()
