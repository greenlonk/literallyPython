import numpy as np
from gameObject import GameObject

class Item(GameObject):

    def __init__(self, gamesize):

        location, type = Item.generate(gamesize)

        super().__init__(location, objecttype=3)
        self.type = type
        self.gamesize: int = gamesize
        self.identify(self.type)
        self.score: int
        self.color: tuple[float]
        
    def identify(self, type):
        match type:
            case 1:
                self.score = 10
                self.color = (255,0,0)
            case 2:
                self.score = 20
                self.color = (0,255,0)
            case 3:
                self.score = 5
                self.color = (0,0,255)
            case _:
                print("Unknown food type!")
    
    def getLocation(self):
        location: list[tuple[int, int]] = self.location
        return location[0]

    def getGameSize(self):
        return self.gamesize

    def getScore(self):
        return self.score
    
    def regenerate(self):
        gamesize = self.getGameSize()
        self.location, self.type = self.generate(gamesize)
        self.identify(self.type)

    @staticmethod
    def generate(gamesize):
        type = np.random.randint(1, 4)
        loc_x = np.random.randint(1, gamesize)
        loc_y = np.random.randint(1, gamesize)
        location: list[tuple] = [(loc_x, loc_y)]
        return location, type