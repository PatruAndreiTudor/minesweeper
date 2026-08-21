import pygame
from sys import exit

def start_timer(screen,start_time):
    current_time = pygame.time.get_ticks() - start_time  #milliseconds
    converted_time = current_time // 1000 #integer
    time_font = pygame.font.Font(None,30) #type,size
    time_surf = time_font.render(f'{converted_time}',False,'Black') #what to display, Anti-Aliasing, Color
    time_rect = time_surf.get_rect(topleft = (225,35))
    pygame.draw.rect(screen,'Grey',time_rect,) #display surf, color, actual rectangle
    screen.blit(time_surf,time_rect)

def initialize_bomb_counter(screen,no_bombs):
    bombs_text_font = pygame.font.Font(None,30)
    bombs_text_surface = bombs_text_font.render(f'{no_bombs}',False,'Black')
    bombs_text_rect = bombs_text_surface.get_rect(topleft = (45,35))
    screen.blit(bombs_text_surface, bombs_text_rect)

def draw_ui(screen):
    screen.fill('Grey')
    pygame.draw.rect(screen,'Light Grey', (15,15,270,60)) #info surf
    pygame.draw.rect(screen,'Light Grey', (15,90,270,270)) #grid surf
    pygame.draw.rect(screen,'Grey', (210,30,60,30)) #time surf
    pygame.draw.rect(screen,'Grey', (130,25,40,40)) #restart surf
    pygame.draw.rect(screen,'Grey', (30,30,60,30)) #bombs surf
    



def main():
    pygame.init()
    pygame.display.set_caption("Minesweeper")
    screen = pygame.display.set_mode((300,375)) #display surface
    clock = pygame.time.Clock() #display refresh time
    game_active = False #check game start
    start_time = 0 #time since init()

    restart_surf = pygame.image.load('graphics/smileyR.png').convert_alpha()
    restart_rect = restart_surf.get_rect(topleft = (130,25))

    while True: #game continues to run until player input stops it
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    print("you have clicked the start button")
                    # this should restart the game, resetting bomb counter,
                    # time counter and the grid to its original state
                    game_active = True
                    start_time = pygame.time.get_ticks()

        draw_ui(screen)
        screen.blit(restart_surf, restart_rect)

        if game_active:
            
            start_timer(screen,start_time) 
            initialize_bomb_counter(screen,10)

        pygame.display.update()
        clock.tick(60)
if __name__ == "__main__":
    main()
