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
        # self.life_c = random.randint(400, 800)
        self.life_c = random.randint(400, 800)
        self.color = [255, 255, 255]
        self.radius = random.randint(3, 5)

        # control partcle center
        if random.random() < 0.2 :
            self.control_obj = True
        else : 
            self.control_obj = False

    def draw(self, tab) :
        if self.life_c > 0 :
            # draw particle
            pygame.draw.circle(tab, self.color, self.position, self.radius)

    def update(self, command) :
        if command == "command_2" and self.control_obj :
            # self.position.xy = 1, 2
            # self.position = self.position + self.velocity
            # self.life_c = self.life_c - 1
            # center = pygame.Vector2(self.position.x/2, self.position.y/2)
            center = pygame.Vector2(640, 360)
            new_velocity = center - self.position
            
            # pulling particle
            if new_velocity.length() > 0 :
                new_velocity.normalize() #
            
            # self.velocity = self.velocity +  (new_velocity * 0.5)
            self.velocity += new_velocity * 0.5

            if self.velocity.length() > 5 :
                self.velocity.scale_to_length(5)
            # color (red/aka)
            self.color = [255, 0, 0]
        else : 
            # self.color = [255, 255, 255]
            if self.color[1] < 255: self.color[1] += 2 
            if self.color[2] < 255: self.color[2] += 2



        # if command == "command_2" : 
        #     print("command_2 worked")
        # if command == "command_3" : 
        #     print("command_3 worked")
        # if command == "command_4" : 
        #     print("command_4 worked")
        # if command == "command_5" : 
        #     print("command_5 worked")
        # else :
        #     # print(command)
        #     self.position = self.position + self.velocity # position with velocity for movement
        #     self.life_c = self.life_c - 1
        self.position = self.position + self.velocity # position with velocity for movement
        self.life_c = self.life_c - 1