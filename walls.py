from gameObject import GameObject

class Walls(GameObject):
    def __init__(self, gamesize):
        location = self.generateWalls(gamesize)
        super().__init__(location, objecttype=2)
        self.length: int = gamesize
        
    def getLocation(self):
        location = self.location
        return location
    
    def getWallSize(self):
        wallsize = self.length
        return wallsize
    
    @staticmethod
    def generateWalls(gamesize):
        coords = (range(0, gamesize+1))

        location: list[tuple] = []
        for i in coords:
            location.append([(i), (0)])
        for i in coords:
            location.append([(i), (gamesize)])
        for i in coords:
            location.append([(gamesize), (i)])
        for i in coords:
            location.append([(0), (i)])
        return location
