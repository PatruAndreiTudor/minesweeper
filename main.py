import pygame
from sys import exit
from cells import Cell
from board import Board
import inspect

def start_timer(screen, start_time, first_click, game_active, end_time = None):
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000 
    time_font = pygame.font.Font(None,30) #type,size
    if first_click:
        time_surf = time_font.render(f'{0:03d}', False, 'Black')
    elif not first_click and game_active:
        time_surf = time_font.render(f'{elapsed_time:03d}',False,'Black') #what to display, Anti-Aliasing, Color
    elif not first_click and not game_active:
        end_time = (end_time - start_time) // 1000
        time_surf = time_font.render(f'{end_time:03d}', False, 'Black')
    time_rect = time_surf.get_rect(topleft = (225,35))
    pygame.draw.rect(screen, 'Grey', time_rect) #display surf, color, actual rectangle
    screen.blit(time_surf, time_rect)

def initialize_bomb_counter(screen, bombs_left):
    bombs_text_font = pygame.font.Font(None,30)
    bombs_text_surface = bombs_text_font.render(f'{bombs_left:03d}', False, 'Black')
    bombs_text_rect = bombs_text_surface.get_rect(topleft = (45,35))
    screen.blit(bombs_text_surface, bombs_text_rect)

def draw_ui(screen):
    screen.fill('Grey')
    pygame.draw.rect(screen, 'Light Grey', (15,15,270,60)) #info surf
    pygame.draw.rect(screen, 'Grey', (210,30,60,30)) #time surf
    pygame.draw.rect(screen, 'Grey', (130,25,40,40)) #restart surf
    pygame.draw.rect(screen, 'Grey', (30,30,60,30)) #bombs surf
    
def main():
    pygame.init()
    pygame.display.set_caption("Minesweeper")
    screen = pygame.display.set_mode((300,375)) #display surface
    clock = pygame.time.Clock() #display refresh time
    game_active = True #check game end (lose or win)
    first_click = True # is this the first click?
    start_time = 0 #time since init()

    cell_images = {
        "smiley": pygame.image.load('graphics/smileyR.png').convert_alpha(),
        "lose": pygame.image.load('graphics/lose.png').convert_alpha(),
        "hidden": pygame.image.load('graphics/hidden.png').convert_alpha(),
        "flagged": pygame.image.load('graphics/flagged.png').convert_alpha(),
        "bomb": pygame.image.load('graphics/bomb.png').convert_alpha(),
        "win": pygame.image.load('graphics/winR.png').convert_alpha(),
        0: pygame.image.load('graphics/empty.png').convert_alpha(),
        1: pygame.image.load('graphics/one.png').convert_alpha(),
        2: pygame.image.load('graphics/two.png').convert_alpha(),
        3: pygame.image.load('graphics/three.png').convert_alpha(),
        4: pygame.image.load('graphics/four.png').convert_alpha(),
        5: pygame.image.load('graphics/five.png').convert_alpha(),
        6: pygame.image.load('graphics/six.png').convert_alpha(),
        7: pygame.image.load('graphics/seven.png').convert_alpha(),
        8: pygame.image.load('graphics/eight.png').convert_alpha(),
    }

    board = Board(rows=9, cols=9, num_bombs=10, size = 30, images=cell_images)
    board.create_grid()
    restart_surf = pygame.image.load('graphics/smileyR.png').convert_alpha()
    restart_rect = restart_surf.get_rect(topleft = (130,25))

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos) and event.button == 1: 
                    board = Board(rows=9, cols=9, num_bombs=10, images=cell_images)
                    board.create_grid()
                    start_time = pygame.time.get_ticks()
                    first_click = True
                    game_active = True
                    restart_surf = cell_images["smiley"]
                else:
                    if game_active and board.rect.collidepoint(event.pos):
                        if first_click:
                            start_time = pygame.time.get_ticks()
                            first_click = False
                        board.handle_click(event.pos, event.button)
                        if board.is_finished:
                            game_active = False
                            restart_surf = board.restart_button
                
        draw_ui(screen)
        screen.blit(restart_surf, restart_rect)
        initialize_bomb_counter(screen, board.get_remaining_bombs())
        start_timer(screen, start_time, first_click, game_active, board.end_time) 
        board.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
