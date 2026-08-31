import pygame
pygame.init()

screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("shooter game")


#set frame rate
clock = pygame.time.Clock()
FPS = 60

#define player actions
moving_left = False
moving_right = False

#define colors
BG = (144, 201, 120)

def draw_bg():
    screen.fill(BG)
    

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.direction = 1
        self.flip = False
        img = pygame.image.load("shoot_game/img/player/Idle/0.png")
        self.image = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        if moving_left:
            dx -= self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx += self.speed
            self.flip = False
            self.direction = 1
        self.rect.x += dx

player = Soldier(200, 200, 3)

run = True
while run:
    clock.tick(FPS)
    draw_bg()
    player.move(moving_left, moving_right)
    player.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        #keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d: 
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_ESCAPE:
                run = False
pygame.quit()