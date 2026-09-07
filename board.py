import pygame
import random
from cells import Cell

class Board(pygame.sprite.Sprite):

    def __init__(self, rows, cols, num_bombs, images, size = 30, offset_pos = (15,90)):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.num_bombs = num_bombs
        self.remaining_cells = self.rows*self.cols - self.num_bombs
        
        self.first_click = True
        self.is_finished = False

        self.surf = pygame.Surface((self.cols*self.size,self.rows*self.size))
        self.rect = self.surf.get_rect(topleft=offset_pos)
        
        self.grid = []
        self.sprite_group = pygame.sprite.Group() #container class to hold and manage multiple Sprite Objects
        
        def handle_click(self,mouse_pos,button):

            if not self.rect.collidepoint(mouse_pos):
                print("Please click on a cell to start the game")
                return

            col_pos = (mouse_pos[0] - self.rect.x)// self.size
            row_pos = (mouse_pos[1] - self.rect.y)// self.size

            clicked_cell = self.grid[row_pos][col_pos]

            if button == 1:
                clicked_cell.reveal()
                self.place_bombs(clicked_cell)
                self.calc_num() #calculate the surrounding bomb count for each empty cell
                self.first_click = False

            if button == 3:
                if not self.first_click:
                    clicked_cell.flag()
                print("You must start the game before flagging a cell")
                return

        def create_grid(self):

            for row in range(self.rows):
                current_row = []
                for col in range(self.cols):
                    new_cell = Cell(cols,rows,self.size,self.images)
                    current_row.append(new_cell)
                    self.sprite_group.add(new_cell)
                self.grid.append(current_row)
                '''
    self.grid[0][0] is the top-left Cell object.
    self.grid[row][col] gives you the cell at any specific row and column.
    self.sprite_group contains all the cells for single-line drawing with self.sprite_group.draw(surface).

                '''
        def board_reveal(self,cell):

            cell.reveal()

            if cell.is_bomb:
                pass # smiley face changes, all bombs are revealed, only the restart button works
                
            if cell.adjacent_bombs == 0:
                col_rev=[-1,0,1]
                row_rev=[-1,0,1]
                for row_pos in row_rev:
                    for col_pos in col_rev:
                        if row_pos == 0 and col_pos == 0:
                            continue
                        


        def place_bombs(self,safe_cell):
            candidates = [ cell for row in self.grid for cell in row if cell != safe_cell]

            bomb_cells = random.sample(candidates,self.num_bombs)

            for cell in bomb_cells:
                cell.is_bomb = True

        def get_remaining_bombs(self):
            flag_count = sum(cell.is_flagged for row in self.grid for cell in row)
            return self.num_bombs - flag_count

        def calc_num(self):


        def generate_board(self, surface):
            self.sprite_group.draw(surface)
            create_grid()
            place_bombs()

        def update(self):
            self.sprite_group.update() #comment
        

