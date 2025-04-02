import pygame, sys
from pygame.locals import *
import random, time

# Initializing pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Defining colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen size and initial variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  # Number of collected coins

# Font settings
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background image
background = pygame.image.load("AnimatedStreet.png")

# Game window
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1, 2, 5])  # Coin weight
        original_image = pygame.image.load("Coin.png")  # Coin texture
        self.image = pygame.transform.scale(original_image, (25, 25))  # Resize to normal size
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Initial position from the top

    def move(self):
        self.rect.move_ip(0, SPEED // 2)  # Coin moves slower than the enemy
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Create game objects
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()

# Add initial coins
for _ in range(3):
    coin = Coin()
    coins.add(coin)

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

# Event to increase enemy speed over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(f"Score: {SCORE}  Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Move all entities
    P1.move()
    E1.move()
    for coin in coins:
        coin.move()

    # Draw all entities
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Coin collection handling
    collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected:
        COINS += coin.weight
        # Add new coin
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

        # Increase enemy speed every 10 coins
        if COINS % 10 == 0:
            SPEED += 1

    # Collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        # Display final score and collected coins under Game Over
        final_score_text = font_small.render(f"Score: {SCORE}  Coins: {COINS}", True, BLACK)
        DISPLAYSURF.blit(final_score_text, (100, 330))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
