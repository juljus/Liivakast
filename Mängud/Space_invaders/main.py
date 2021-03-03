import pygame
import random
import math

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("space_background.jpg")

# title
pygame.display.set_caption("Space Invaders")

# player
playerImg = pygame.image.load("player.png")
playerX = 368
playerY = 500
playerX_change = 0

# enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(50, 750)
enemyY = random.randint(25, 150)
enemyX_change = 0.1
enemyY_change = 64

# bullet
bulletImg = pygame.image.load("lazer_bullet.png")
bulletX = 0
bulletY = 500
bulletX_change = 2
bulletY_change = 1
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 32, y + 20))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# game loop
running = True
while running:

    # RGB = Red, Green, Blue (up to 255 for each value)
    screen.fill((255, 255, 255))

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # controlling the spaceship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                else:
                    pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyY += enemyY_change
        enemyX_change = 1.5
    elif enemyX >= 736:
        enemyY += enemyY_change
        enemyX_change = -1.5

    # bullet movement

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
