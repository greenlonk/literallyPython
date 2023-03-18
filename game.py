import os
import pygame
from snake import Snake
from items import Item
from walls import Walls
from graphicsEngine import GraphicsEngine

class Game():

    running: bool=False
    sleep: float = 1. 
    runtime: int = 0

    def __init__(self, snake, item, walls, engine, HIGHSCORE_FILE):
        self.running: bool = Game.running       
        self.score: int = 0
        self.snake: Snake = snake
        self.item: Item = item
        self.walls: Walls = walls
        self.engine: GraphicsEngine = engine
        self.highscore_file = HIGHSCORE_FILE
        self.highscore: int = 0

    def start_game(self):
        self.running = True
        self.engine.add_object(self.snake)
        self.engine.add_object(self.item)
        self.engine.add_object(self.walls)
        self.load_highscore()
        self.gameloop()

    def gameloop(self):
        clock = pygame.time.Clock()
        clock.tick(20) # Giving the Engine enough time to initalize

        while self.running:
            clock.tick(60)
            self.check_collisions()
            self.engine.update_screen()
            Game.runtime += 1
            if (Game.runtime == 7):

                self.snake.move()
                Game.runtime = 0

            for event in pygame.event.get():
                self.handleInput(event)

            score = self.getScore()
            if score > self.highscore:
                self.highscore = score
                self.save_highscore()

        self.engine.close()

    def quit_game(self):
        self.running = False
        

    def handleInput(self, event: pygame.event.EventType):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.snake.getDirection() != "down":
                self.snake.setDirection("up")
            elif event.key == pygame.K_DOWN and self.snake.getDirection() != "up":
                self.snake.setDirection("down")
            elif event.key == pygame.K_LEFT and self.snake.getDirection() != "right":
                self.snake.setDirection("left")
            elif event.key == pygame.K_RIGHT and self.snake.getDirection() != "left":
                self.snake.setDirection("right")
            else:
                pass

    def check_collisions(self): # Checks for different types of collisions
        
        head: tuple[int, int] = self.snake.getHead()
        body: list[tuple[int, int]] = self.snake.getBody()
        item: tuple[int, int] = self.item.getLocation()
        wallsize: int = self.walls.getWallSize()

        if (Game.tuple_in_list(head, body)): # snake head collides with snake body
            print("Too hungry?")
            self.quit_game()
            return
       
        if (head == item): # snake head collides with item
            self.snake.grow()
            self.setScore(self.getScore() + self.item.getScore()) 
            self.item.regenerate()
            print("Item found! New Score: " + str(self.getScore()))
       
        if (Game.check_bounds(item, wallsize)): # item collides with walls
            self.item.regenerate()
            print("Item regenerated.")

        if (Game.check_bounds(head, wallsize)): # snake collides with walls
            print("Game Over!")
            self.quit_game()
            return
     
        else: # Debugging
            pass

    def getScore(self):
        return self.score
    
    def setScore(self, score):
        self.score = score
    
    def load_highscore(self):
        if os.path.isfile(self.highscore_file):
            with open(self.highscore_file, "r") as f:
                self.highscore = int(f.read().strip())

    def save_highscore(self):
        with open(self.highscore_file, "w") as f:
            f.write(str(self.highscore))

    @staticmethod
    def check_bounds(item: tuple[int, int], wallsize: int) -> bool:
        x, y = item
        if ((x <= 0) or (x >= wallsize)):
            return True
        if ((y <= 0) or (y >= wallsize)):
            return True
        return False

    @staticmethod
    def tuple_in_list(myTuple: tuple[int, int], myList: list[tuple[int, int]]) -> bool:
        for item in myList:
            if item == myTuple:
                return True
        return False

