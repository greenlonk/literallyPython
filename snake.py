from gameObject import GameObject

class Snake(GameObject):

    def __init__(self):
        location: list[tuple] = [(5,5), (6,5), (7,5)]
        super().__init__(location, objecttype=1)
        self.direction: str = "right"
        self.length: int = len(self.location)
        self.growing: bool = False
        self.head: list[tuple] = self.location[-1]

    def move(self):
        ## Move forward in the direction given
        head = self.head
        match (self.direction):
            case "right":
                new_head = (head[0]+1, head[1])
            case "left":
                new_head = (head[0]-1, head[1])
            case "down":
                new_head = (head[0], head[1]+1)
            case "up":
                new_head = (head[0], head[1]-1)
        self.location.append(new_head)
        self.head = new_head

        if (self.growing == True):
            self.growing = False
        elif (self.growing == False):
            self.location = self.location[1:]

    def grow(self):
        self.growing = True
    
    def getLocation(self):
        location = self.location
        return location
    
    def getHead(self):
        loc = self.location[-1]
        return loc
    
    def getBody(self):
        loc = self.location[0:-1]
        return loc
    
    def setDirection(self, dir: str):
        self.direction = dir

    def getDirection(self):
        return self.direction
