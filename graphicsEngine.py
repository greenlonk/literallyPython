import pygame
from decorators import debug


class GraphicsEngine:
    def __init__(self, width: int, height: int, scaling_factor: int):
        pygame.init()
        self.width = width
        self.height = height
        self.scaling_factor = scaling_factor
        self.objects: list = []
        self.window = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Literally (a) Python")

    def add_object(self, obj):
        self.objects.append(obj)

    def _render_objects(self):

        for obj in self.objects:
            obj_color = obj.getColor()

            if (obj.objecttype==1 or obj.objecttype==2):
                for segment in obj.getLocation(): 
                    pygame.draw.rect(self.window, obj_color, pygame.Rect(float(segment[0]*self.scaling_factor), float(segment[1]*self.scaling_factor), float(self.scaling_factor), float(self.scaling_factor)))
            elif (obj.objecttype==3):
                pygame.draw.rect(self.window, obj_color, pygame.Rect(float(obj.getLocation()[0]*self.scaling_factor),float(obj.getLocation()[1]*self.scaling_factor), float(self.scaling_factor), float(self.scaling_factor)))
       
        pygame.display.update()

    def clear_screen(self):
        self.window.fill((255, 255, 255))

    def update_screen(self):
        self.clear_screen()
        self._render_objects()
        
    def close(self):
        pygame.quit()