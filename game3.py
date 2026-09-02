import os
import pygame

# Start Pygame
pygame.init()

# Create the game window
screen_width = 800
screen_height = int(screen_width * 0.8)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooter Game")

# Set the game speed
clock = pygame.time.Clock()
FPS = 60

# Game settings
BG = (144, 201, 120)
GROUND_COLOR = (170, 130, 80)
GROUND_Y = 500
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def draw_bg():
    """Draw the background and ground."""
    screen.fill(BG)

    # Draw the ground
    pygame.draw.rect(
        screen,
        GROUND_COLOR,
        (0, GROUND_Y, screen_width, screen_height - GROUND_Y),
    )

    # Draw the top line of the ground
    pygame.draw.line(
        screen,
        (100, 80, 50),
        (0, GROUND_Y),
        (screen_width, GROUND_Y),
        3,
    )


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale):
        super().__init__()

        # Player settings
        self.alive = True
        self.char_type = char_type
        self.speed = 5
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.flip = False

        # Animation settings
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_list = []

        # Animation folders and frame counts
        animation_types = [
            ("Idle", 5),
            ("Run", 6),
        ]

        # Load all animation images
        for folder, frame_count in animation_types:
            temp_list = []

            for i in range(frame_count):
                path = os.path.join(
                    BASE_DIR,
                    "shoot_game",
                    "img",
                    self.char_type,
                    folder,
                    f"{i}.png",
                )

                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(
                    img,
                    (
                        int(img.get_width() * scale),
                        int(img.get_height() * scale),
                    ),
                )
                temp_list.append(img)

            self.animation_list.append(temp_list)

        # Set the starting image and position
        self.image = self.animation_list[0][0]
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, moving_left, moving_right):
        """Move the soldier and apply gravity."""
        dx = 0

        # Move left or right
        if moving_left:
            dx -= self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx += self.speed
            self.flip = False
            self.direction = 1

        # Start a jump
        if self.jump:
            self.vel_y = -11
            self.jump = False

        # Apply gravity
        self.vel_y += 0.5
        dy = self.vel_y

        self.rect.x += dx
        self.rect.y += dy

        # Stop the soldier at the ground
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0

        # Choose idle or running animation
        self.update_action(1 if dx != 0 else 0)

    def update_action(self, new_action):
        """Change the current animation."""
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def update_animation(self):
        """Switch to the next animation frame."""
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

            # Restart the animation when it reaches the end
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

            self.image = self.animation_list[self.action][self.frame_index]

    def draw(self, surface):
        """Draw the soldier on the screen."""
        image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(image, self.rect)


# Create the player and enemy
player = Soldier("player", 200, 200, 3)
enemy = Soldier("enemy", 400, 200, 3)

moving_left = False
moving_right = False
run = True

# Main game loop
while run:
    clock.tick(FPS)

    # Handle keyboard and window events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_SPACE and player.rect.bottom >= GROUND_Y:
                player.jump = True
            elif event.key == pygame.K_ESCAPE:
                run = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_d:
                moving_right = False

    # Draw the background and ground
    draw_bg()

    # Update the player
    player.move(moving_left, moving_right)
    player.update_animation()
    player.draw(screen)

    # Keep the enemy standing on the ground
    enemy.move(False, False)
    enemy.update_animation()
    enemy.draw(screen)

    pygame.display.update()

# Close Pygame
pygame.quit()