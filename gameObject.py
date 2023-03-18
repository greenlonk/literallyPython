## Object types:
## 1 -> snake
## 2 -> wall
## 3 -> item

class GameObject():
    
    def __init__(self, location, objecttype):
        self.location: list[tuple] = location
        self.objecttype: int = objecttype
        self.color: tuple[float]

        match(self.objecttype):
                case 1: #snake
                    self.color = (0, 0, 0)
                case 2: #wall
                    self.color = (128, 0, 128)
                case 3: #item (unneccesary)
                    self.color = (128, 128, 128)
                case _:
                    self.color = (64, 64, 64)

    def getColor(self):
        color = self.color
        return color

 