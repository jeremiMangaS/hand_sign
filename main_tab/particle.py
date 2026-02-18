import pygame
import random

class Particle :
    # self : refer the object
    def __init__(self, x):
        # random spawn position
        set_pos_x = random.randint(1, x)
        set_pos_y= random.randint(1, x)
        self.position = pygame.Vector2(set_pos_x, set_pos_y)
        # to accsess decimal value between -1 to 1 for x and y
        self.velocity = pygame.Vector2(random.uniform(-3, 3), 
                                       random.uniform(-3, 3))
        # self.life_c = [70, 100]
        self.life_c = random.randint(1400, 1600)
        self.color = [255, 255, 255]
        self.radius = random.randint(3, 5)

    def draw(self, tab) :
        if self.life_c > 0 :
            # draw particle
            pygame.draw.circle(tab, self.color, self.position, self.radius)

    def update(self) :
        self.position = self.position + self.velocity # position with velocity for movement
        self.life_c = self.life_c - 1