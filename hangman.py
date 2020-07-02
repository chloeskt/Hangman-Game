import pygame

#setup display
pygame.init()
#define constant values
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

#colors
WHITE = (255, 255, 255)

#load images
images = []
for i in range(7):
    images.append(pygame.image.load("images/hangman" + str(i) + ".png"))

#game variables 
hangman_status = 0 


#setup game loop
FPS = 60 #max FPS
clock = pygame.time.Clock()
run = True 

while run:
    #play game 
    clock.tick(FPS)

    #win.fill((12, 123, 88))
    win.fill(WHITE)
    win.blit(images[hangman_status], dest=(150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()