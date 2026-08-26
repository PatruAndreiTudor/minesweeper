import pygame
from cells import Cell

class Board(pygame.sprite.Sprite):

    def __init__(self,rows,cols,num_bombs,cell_size,images):
        super().__init__()
        self.remaining_cells = None
        self.is_started = True
        self.is_finished = False
        self.num_bombs = num_bombs

        self.first_click = True
        self.grid = []
        self.sprite_group = pygame.sprite.Group() #container class to hold and manage multiple Sprite Objects

        def draw(self, surface):
            self.sprite_group.draw(surface)

        def update(self):
            self.sprite_group.update()
        

