from game import Game
from graphicsEngine import GraphicsEngine
from snake import Snake
from items import Item
from walls import Walls

HIGHSCORE_FILE = "highscore.txt"

gamesize: int = 64
windowsize: int = 780
scaling_factor = windowsize // gamesize

mySnake = Snake()
myItem = Item(gamesize)
myWalls = Walls(gamesize)
myEngine = GraphicsEngine(windowsize, windowsize, scaling_factor)
myGame = Game(mySnake, myItem, myWalls, myEngine, HIGHSCORE_FILE)

myGame.start_game()   