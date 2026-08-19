import pygame
from sys import exit

def start_timer(screen):
    current_time = pygame.time.get_ticks()  #milliseconds
    converted_time = current_time // 1000 #integer
    time_font = pygame.font.Font(None,30) #type,size
    time_surf = time_font.render(f'{converted_time}',False,'Black') #what to display, Anti-Aliasing, Color
    time_rect = time_surf.get_rect(topleft = (225,35))
    pygame.draw.rect(screen,'Grey',time_rect,) #display surf, color, actual rectangle
    
    screen.blit(time_surf,time_rect)


def main():
    pygame.init()
    pygame.display.set_caption("Minesweeper")
    screen = pygame.display.set_mode((300,375)) #display surface
    clock = pygame.time.Clock() #display refresh time
    bkg_surf= pygame.Surface((300,375))
    bkg_surf.fill('Grey')
    info_surf= pygame.Surface((270,60))
    info_surf.fill('Light Grey')
    board_surf= pygame.Surface((270,270))
    board_surf.fill('Light Grey')
    time_box=pygame.Surface((60,30))
    time_box.fill('Grey')
    restart_box=pygame.Surface((45,40))
    restart_box.fill('Grey')
    remaining_bombs_box=pygame.Surface((60,30))
    remaining_bombs_box.fill('Grey')

    while True: #game continues to run until player input stops it
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.blit(bkg_surf,(0,0))
        screen.blit(info_surf, (15,15))
        screen.blit(board_surf, (15,90))
        screen.blit(time_box, (210,30))
        screen.blit(restart_box, (120,25))
        screen.blit(remaining_bombs_box, (30,30))
        start_timer(screen) #always starts, need to start when the first move is made

        pygame.display.update()
        clock.tick(60)
if __name__ == "__main__":
    main()
