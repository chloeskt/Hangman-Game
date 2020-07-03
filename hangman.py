import pygame
import math
import nltk
nltk.download('words')
from nltk.corpus import words
import random

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
WORD_FONT = pygame.font.SysFont("arial", 60)
TITLE_FONT = pygame.font.SysFont('arial', 70)

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
wordlist = words.words()
random.shuffle(wordlist)
length = True
while length:
    word = random.choice(wordlist).upper()
    if len(word) > 4 and len(word) < 8:
        length = False
guessed = []
print(word.upper())

def draw():
    """
    Draw the game
    """
    win.fill(WHITE)
    text = TITLE_FONT.render("Hangman game", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word.upper():
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, GREEN)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLUE, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message, color):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, color)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(4000)

            
def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            display_message("You're a winner !!", color=GREEN)
            break

        if hangman_status == 6:
            display_message("Sorry, you lost :( ", color=RED)
            break
    
while True:
    main()
    ###TODO: make a menu for the user, to know if he.she wants to play again or quit
    #need to make changes to some var: hangman_status, guessed, word, --> write a function for game variables 
    #last: make a class
pygame.quit()