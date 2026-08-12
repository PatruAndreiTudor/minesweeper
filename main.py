import pygame
from sys import exit

def main():
    pygame.init()
    pygame.display.set_caption("Minesweeper")
    screen = pygame.display.set_mode((1280,720)) #display surface
    clock = pygame.time.Clock() #display refresh time
    
    while True: #game continues to run until player input stops it
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        pygame.display.update()
        clock.tick(60)

