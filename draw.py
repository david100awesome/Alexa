import pygame

pygame.init()

display_width = 1000
display_height = 1000

pikaDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pikachu')

pikachu_normal = pygame.transform.scale((pygame.image.load("pikachu normal.png")), (1000, 1000))
pikachu_hi = pygame.transform.scale((pygame.image.load("pikachu hi.jpg")), (1000, 1000))
pikachu_pose = pygame.transform.scale((pygame.image.load("pikachu pose.png")), (1000, 1000))
pikachu_attack = pygame.transform.scale((pygame.image.load("pikachu attack.png")), (1000, 1000))

def normal_pic():
    pikaDisplay.fill((255,255,255))
    pikaDisplay.blit(pikachu_normal, (0,0))
    pygame.display.update()

def hi_pic():
    pikaDisplay.fill((255,255,255))
    pikaDisplay.blit(pikachu_hi, (0,0))
    pygame.display.update()

def pose_pic():
    pikaDisplay.fill((255,255,255))
    pikaDisplay.blit(pikachu_pose, (0,0))
    pygame.display.update()

def attack_pic():
    pikaDisplay.fill((255,255,255))
    pikaDisplay.blit(pikachu_attack, (0,0))
    pygame.display.update()
    
def exit_key():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()