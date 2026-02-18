import pygame
import particle
# import random

# window shape
W_WIDTH = 1280
W_HWIGHT = 720
# w_center = W_WIDTH/2
# h_center = W_HWIGHT/2

# particles
particles_list = []


pygame.init() # window/tab initialization
screen = pygame.display.set_mode((W_WIDTH, W_HWIGHT))
# screen = pygame.display.set_mode()
pygame.display.set_caption('main tab')
clock = pygame.time.Clock()
running = True

# main loop
while running :
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :  
            running = False
        
    screen.fill("black") # cleaner

    # spawing the particle
    prtcl1_obj = particle.Particle(W_WIDTH)
    prtcl2_obj = particle.Particle(W_WIDTH)
    prtcl3_obj = particle.Particle(W_WIDTH)
    particles_list.append(prtcl1_obj)
    particles_list.append(prtcl2_obj)
    particles_list.append(prtcl3_obj)

    for i in particles_list :
        i.update()
        i.draw(screen)
        if i.life_c < 1 :
            particles_list.remove(i)

    pygame.display.flip()

    clock.tick(120)
pygame.quit()