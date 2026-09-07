import pygame


class Cell(pygame.sprite.Sprite):

    def __init__(self, cols, rows, images, size = 30):
        super().__init__()
        
        self.cols = cols
        self.rows = rows
        self.images = images
        self.is_bomb = is_bomb
        
        self.__is_revealed = False
        self.__is_flagged = False
        self.adjacent_bombs = 0

        self.image = self.images["hidden"]
        self.rect = self.image.get_rect(topleft = (self.cols * self.size, self.rows * self.size)) 
        
        def reveal(self):
            if self.__is_flagged or self.__is_revealed:
                print("Cannot reveal a flagged or an already revealed cell")
                return 
            else:
                self.__is_revealed = True
                if self.is_bomb:
                    self.image = self.images["bomb"] 
                else:
                    self.image = self.images[self.adjacent_bombs] 

        def flag(self):
            if self.__is_revealed:
                print ("Cannot flag a revealed cell")
                return
            if self.__is_flagged:
                self.__is_flagged = False
                self.image = self.images["hidden"]
            else:
                self.__is_flagged = True
                self.image = self.images["flagged"]
        
