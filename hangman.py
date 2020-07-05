import pygame
import math
import nltk
nltk.download('words')
from nltk.corpus import words
import random
import os

#setup display
pygame.init()

pygame.font.init()

#define constant values
WIDTH, HEIGHT = 800, 500
#win = pygame.display.set_mode((WIDTH, HEIGHT))
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
letters = [] 
start_x = round((WIDTH - (GAP + RADIUS*2)*13)/2)
start_y = 400

for i in range(26):
    x = start_x + GAP*2 + ((RADIUS*2 + GAP) * (i % 13))
    y = start_y + ((i // 13) * (GAP + RADIUS*2))
    letters.append([x, y, chr(65 + i), True])

#game variables 
#hangman_status = 0 
#wordlist = words.words()
#random.shuffle(wordlist)
#length = True
#while length:
#    word = random.choice(wordlist).upper()
#    if len(word) > 4 and len(word) < 8:
#        length = False
#guessed = []

class Main_Menu():
    #start_btn = pygame.image.load('images/button_play.png')
    #logo = pygame.image.load('images/logo.png')  
    
    def __init__(self, win):
        self.width = 800
        self.height = 500
        self.bg = pygame.image.load('images/background.png')
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.start_btn = pygame.image.load('images/button_play.png')
        self.logo = pygame.image.load('images/logo.png') 
        self.btn = (self.width/2 - self.start_btn.get_width()/2, 350, self.start_btn.get_width(), self.start_btn.get_height())

    def run(self):
        run = True 

        while run: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.house.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = HangmanGame(self.win)
                            game.main()
                            del game
            self.draw()
            
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.win.blit(self.logo, (self.width/2 - self.logo.get_width()/2, 0))
        self.win.blit(self.start_btn, (self.btn[0], self.btn[1]))
        pygame.display.update()

class HangmanGame():

    def __init__(self, win):
        self.WIDTH = 800
        self.HEIGHT = 500
        self.win = win 
        self.hangman_status = 0
        self.RADIUS = 20
        self.GAP = 15

    def draw(self):
        """
        Draw the game
        """
        win.fill(WHITE)
        text = TITLE_FONT.render("Hangman game", 1, BLACK)
        win.blit(text, (self.WIDTH/2 - text.get_width()/2, 20))

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
                pygame.draw.circle(win, BLUE, (x, y), self.RADIUS, 3)
                text = LETTER_FONT.render(ltr, 1, BLACK)
                win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

        win.blit(images[self.hangman_status], (150, 100))
        pygame.display.update()

    def display_message(self, message, color):
        pygame.time.delay(1000)
        win.fill(WHITE)
        text = WORD_FONT.render(message, 1, color)
        win.blit(text, (self.WIDTH/2 - text.get_width()/2, self.HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(4000)

    def pick_word(self):
        wordlist = words.words()
        random.shuffle(wordlist)
        length = True
        while length:
            word = random.choice(wordlist).upper()
            if len(word) > 4 and len(word) < 8:
                length = False
        #guessed = []
        return word
            
    def main(self):

        FPS = 60
        clock = pygame.time.Clock()
        run = True

        while run:
            guessed = []
            word = pick_word()
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
                            if dis < self.RADIUS:
                                letter[3] = False
                                guessed.append(ltr)
                                if ltr not in word:
                                    self.hangman_status += 1
            
            draw()

            won = True
            for letter in word:
                if letter not in guessed:
                    won = False
                    break
            
            if won:
                display_message("You're a winner !!", color=GREEN)
                break

            if self.hangman_status == 6:
                display_message("Sorry, you lost :( ", color=RED)
                break
    
#while True:
#    main()
    #TODO: make a menu for the user, to know if he.she wants to play again or quit, and choose language?
    #need to make changes to some var: hangman_status, guessed, word, --> write a function for game variables 
    #last: make a class
#pygame.quit()

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    #from main_menu.main_menu import Main_Menu
    mainMenu = Main_Menu(win)
    Main_Menu.run()