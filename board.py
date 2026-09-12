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
        self.size = size
        self.end_time = None
        self.first_click = True
        self.game_active = True
        self.images = images
        self.is_finished = False
        self.surf = pygame.Surface((self.cols*self.size, self.rows*self.size))
        self.rect = self.surf.get_rect(topleft=offset_pos)
        self.restart_button = self.images["smiley"]
        self.grid = []
        self.sprite_group = pygame.sprite.Group() #container class to hold and manage multiple Sprite Objects
        
    def create_grid(self):
        for row in range(self.rows):
            current_row = []
            for col in range(self.cols):
                new_cell = Cell(col, row, self.images, self.size)
                current_row.append(new_cell)
                self.sprite_group.add(new_cell)
            self.grid.append(current_row)

    def handle_click(self, mouse_pos, button):
        if not self.rect.collidepoint(mouse_pos):
            print("Please click on a cell to start the game")
            return
            #^^ might be redundant due to the guarding if in main
        col_pos = (mouse_pos[0] - self.rect.x)// self.size
        row_pos = (mouse_pos[1] - self.rect.y)// self.size
        clicked_cell = self.grid[row_pos][col_pos]
        if button == 1 and self.first_click and self.game_active:
            self.place_bombs(clicked_cell)
            self.calc_num() #calculate the surrounding bomb count for each empty cell
            self.first_click = False
            self.board_reveal(clicked_cell)
        elif button == 1 and self.game_active:
            self.board_reveal(clicked_cell)
        elif button == 1 and not self.game_active:
            print("The game is over")
            return
        if button == 3:
            if not self.first_click and self.game_active:
                clicked_cell.flag()
            elif not self.game_active:
                print("The game is over")
                return
            elif self.first_click:
                print("You must start the game before flagging a cell")
                return

    def board_reveal(self, cell):
        if cell.is_flagged:
            print("You cannot reveal a flagged cell")
            return
        cell.reveal()    
        if cell.is_bomb:
            bombs = [ cell for row in self.grid for cell in row if cell.is_bomb]
            for bomb in bombs:
                bomb.reveal()
                if bomb.is_flagged:
                    bomb.image = bomb.images["bomb"] 
            self.game_active = False
            self.end_time = pygame.time.get_ticks()
            self.is_finished = True
            self.restart_button = self.images["lose"]
            print("You lost!")
            return
        if cell.adjacent_bombs == 0:
            neighbors = self.get_neighbors(cell)
            for neighbor in neighbors:
                if not neighbor.is_revealed:
                    self.board_reveal(neighbor)
        total_revealed = sum ( 1 for row in self.grid for item in row if item.is_revealed)
        if total_revealed == (self.rows * self.cols) - self.num_bombs:
            self.game_active = False
            self.end_time = pygame.time.get_ticks()
            self.is_finished = True
            self.restart_button = self.images["win"]
            print("You won!")
            return
     
    def place_bombs(self, safe_cell):
        neighbors = self.get_neighbors(safe_cell)
        neighbors.append(safe_cell)
        candidates = [ cell for row in self.grid for cell in row if cell not in neighbors]
        bomb_cells = random.sample(candidates, self.num_bombs)
        for cell in bomb_cells:
            cell.is_bomb = True

    def get_remaining_bombs(self):
        flag_count = sum(cell.is_flagged for row in self.grid for cell in row)
        total = self.num_bombs - flag_count
        if total <= 0:
            return 0
        return total

    def get_neighbors(self, cell):
        neighbors=[]
        col_neighbor=[-1,0,1]
        row_neighbor=[-1,0,1]
        for row in row_neighbor:
            for col in col_neighbor:
                if row == 0 and col == 0:
                    continue
                neighbor_c=cell.cols + col
                neighbor_r=cell.rows + row
                if 0 <= neighbor_c < self.cols and 0 <= neighbor_r < self.rows:
                    neighbors.append(self.grid[neighbor_r][neighbor_c])
        return neighbors

    def calc_num(self):
        bomb_cells = [ cell for row in self.grid for cell in row if cell.is_bomb]
        for bomb in bomb_cells:
            bomb_neighbors = self.get_neighbors(bomb)
            for neighbor in bomb_neighbors:
                if not neighbor.is_bomb:
                    neighbor.adjacent_bombs+=1

    def draw(self, screen):
        self.sprite_group.draw(self.surf)
        screen.blit(self.surf, self.rect)
        

