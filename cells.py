import pygame


class Cell(pygame.sprite.Sprite):

    def __init__(self, col, row, size, images):
        super().__init__()
        
        self.col = col
        self.row = row
        self.images = images
        
        self.is_revealed = False
        self.is_flagged = False
        self.is_bomb = False
        self.adjacent_bombs = 0

        self.image = self.images["hidden"]
        self.rect = self.image.get_rect(topleft = (col*size, row*size)) 
        
        def reveal(self):
            if self.is_flagged:
                return 
            if not self.is_revealed:
                self.is_revealed = True
                if self.is_bomb:
                    self.image = self.images["bomb"] #it should trigger game loss
                else:
                    self.image = self.images[self.adjacent_bombs] #val of 0 should trigger cascading reveal
                    #if there are no more hidden cells, you win!

        def flag(self):

            if self.is_revealed:
                return
            if self.is_flagged:
                self.is_flagged = False
                self.image = self.images["hidden"]
            else:
                self.is_flagged = True
                self.image = self.images["flagged"]
        
