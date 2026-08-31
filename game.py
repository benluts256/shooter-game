import pygame
pygame.init()

window = pygame.display.set_mode((1000,600))
color = (15,30,60)
window.fill(color)

player = pygame.Rect(300,300,50,50)
bg_img = pygame.image.load('bg_10.jpg')
bg_img = pygame.transform.scale(bg_img,(1000,600))
brick_txt = pygame.image.load('bg_11.jpg')
brick_txt = pygame.transform.scale(brick_txt,(100,100))

running = True
while running:
    window.blit(bg_img,(0,0))

    pygame.draw.rect(window,(0,128,128),pygame.Rect(0,580,1000,20)) #level 1
    pygame.draw.rect(window,(0,128,128),pygame.Rect(0,430,750,20)) #level 2
    pygame.draw.rect(window,(0,128,128),pygame.Rect(0,280,200,20)) #level 3A
    pygame.draw.rect(window,(0,128,128),pygame.Rect(300,280,700,20)) #level 3B
    pygame.draw.rect(window,(0,128,128),pygame.Rect(0,130,700,20)) #level 4A
    pygame.draw.rect(window,(0,128,128),pygame.Rect(820,130,180,20)) #level 4B
