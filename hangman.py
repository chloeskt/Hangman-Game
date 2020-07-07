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
pygame.display.set_caption("Hangman Game")

#colors
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

#fonts
LETTER_FONT = pygame.font.SysFont("arial", 40)
WORD_FONT = pygame.font.SysFont("arial", 60)
TITLE_FONT = pygame.font.SysFont('arial', 70)

class Main_Menu():
    
    def __init__(self, win):
        self.width = 800
        self.height = 500
        self.win = win
        self.start_btn = pygame.image.load('images/play.png')
        self.logo = pygame.image.load('images/logo.png') 
        self.btn = (625, 300, self.start_btn.get_width(), self.start_btn.get_height())
        self.first_game = True
        self.replay_btn = pygame.image.load('images/replay_button.png')


    def run(self):
        run = True 

        while run: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = HangmanGame(self.win)
                            game.main()
                            del game
                            self.first_game = False
            
            self.draw()

            
        pygame.quit()

    def draw(self):
        self.win.fill(WHITE)
        self.win.blit(self.logo, (180,75))
        if self.first_game:
            self.win.blit(self.start_btn, (620, 300))
        else:
            self.win.blit(self.replay_btn, (620, 300))
        text = TITLE_FONT.render("Hangman game", 1, BLACK)
        self.win.blit(text, (self.width/2 - text.get_width()/2, 20))
        pygame.display.update()

class HangmanGame():

    def __init__(self, win):
        self.WIDTH = 800
        self.HEIGHT = 500
        self.win = win 
        self.hangman_status = 0
        self.RADIUS = 20
        self.GAP = 15
        self.word = None
        self.guessed = []
        self.images = []
        for i in range(7):
            self.images.append(pygame.image.load("images/hangman" + str(i) + ".png"))
        self.letters = [] 
        self.start_x = round((WIDTH - (GAP + RADIUS*2)*13)/2)
        self.start_y = 400
        for i in range(26):
            x = self.start_x + self.GAP*2 + ((self.RADIUS*2 + self.GAP) * (i % 13))
            y = self.start_y + ((i // 13) * (self.GAP + self.RADIUS*2))
            self.letters.append([x, y, chr(65 + i), True])

    def draw(self):
        """
        Draw the game
        """
        self.win.fill(WHITE)
        text = TITLE_FONT.render("Hangman game", 1, BLACK)
        self.win.blit(text, (self.WIDTH/2 - text.get_width()/2, 20))

        # draw word
        display_word = ""
        for letter in self.word.upper():
            if letter in self.guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        text = WORD_FONT.render(display_word, 1, GREEN)
        win.blit(text, (400, 200))

        # draw buttons
        for letter in self.letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(win, BLUE, (x, y), self.RADIUS, 3)
                text = LETTER_FONT.render(ltr, 1, BLACK)
                win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

        win.blit(self.images[self.hangman_status], (150, 100))
        pygame.display.update()

    def display_message(self, message, color):
        pygame.time.delay(1000)
        self.win.fill(WHITE)
        text = WORD_FONT.render(message, 1, color)
        self.win.blit(text, (self.WIDTH/2 - text.get_width()/2, self.HEIGHT/2 - text.get_height()/2))
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
        return word 
            
    def main(self):

        FPS = 60
        clock = pygame.time.Clock()
        run = True
        self.word = self.pick_word()
        print('WORD', self.word)

        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    for letter in self.letters:
                        x, y, ltr, visible = letter
                        if visible:
                            dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                            if dis < self.RADIUS:
                                letter[3] = False
                                self.guessed.append(ltr)
                                if ltr not in self.word:
                                    self.hangman_status += 1
            
            self.draw()

            won = True
            for letter in self.word:
                if letter not in self.guessed:
                    won = False
                    break
            
            if won:
                self.display_message("You're a winner !!", color=GREEN)
                break

            if self.hangman_status == 6:
                self.display_message("Sorry, you lost :( ", color=RED)
                break


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    mainMenu = Main_Menu(win)
    mainMenu.run()