import pygame


class Cell(pygame.sprite.Sprite):

    def __init__(self, cols, rows, images, size = 30):
        super().__init__()
        
        self.cols = cols
        self.rows = rows
        self.images = images
        self.is_bomb = False
        self.size = size
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_bombs = 0
        self.image = self.images["hidden"]
        self.rect = self.image.get_rect(topleft = (self.cols * self.size, self.rows * self.size)) 
        
    def reveal(self):
            if self.is_flagged or self.is_revealed:
                print("Cannot reveal a flagged or an already revealed cell")
                return 
            else:
                self.is_revealed = True
                if self.is_bomb:
                    self.image = self.images["bomb"] 
                else:
                    self.image = self.images[self.adjacent_bombs] 

    def flag(self):
            if self.is_revealed:
                print ("Cannot flag a revealed cell")
                return
            if self.is_flagged:
                self.is_flagged = False
                self.image = self.images["hidden"]
            else:
                self.is_flagged = True
                self.image = self.images["flagged"]
        
