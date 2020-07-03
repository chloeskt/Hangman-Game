import pygame
import math as m

#setup display
pygame.init()
#define constant values
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

#colors
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

#load images
images = []
for i in range(7):
    images.append(pygame.image.load("images/hangman" + str(i) + ".png"))

#fonts
LETTER_FONT = pygame.font.SysFont("arial", 40)

#letters font
RADIUS = 20
GAP = 15
letters = [] #the alphabet
start_x = round((WIDTH - (GAP + RADIUS*2)*13)/2)
start_y = 400
#A = 65
for i in range(26):
    x = start_x + GAP*2 + ((RADIUS*2 + GAP) * (i % 13))
    y = start_y + ((i // 13) * (GAP + RADIUS*2))
    letters.append([x, y, chr(65 + i), True])

#game variables 
hangman_status = 0 


#setup game loop
FPS = 60 #max FPS
clock = pygame.time.Clock()
run = True 


def draw():
    """
    Draw the game
    """
    win.fill(WHITE)

    for letter in letters: 
        x, y, char, visible = letter
        if visible: 
            pygame.draw.circle(win, BLUE, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(char, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], dest=(150, 100))
    pygame.display.update()



while run:
    #play game 
    clock.tick(FPS)

    #win.fill((12, 123, 88))
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters: 
                x, y, char, visible = letter 
                if visible:
                    dis = m.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False 
            

pygame.quit()