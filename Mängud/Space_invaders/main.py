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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8

for counter in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(6, 730))
    enemyY.append(random.randint(25, 150))
    enemyX_change.append(7)
    enemyY_change.append(64)

# bullet
bulletImg = pygame.image.load("laser_bullet.png")
bulletX = 0
bulletY = 500
bulletX_change = 2
bulletY_change = 10
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font("space age.ttf", 32)

textX = 10
textY = 10

# game over text
over_font = pygame.font.Font("space age.ttf", 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(over_text, (175, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 30, y + 20))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    pygame.time.delay(50)

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
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
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
    for ix in range(num_of_enemies):

        # game over
        if enemyY[ix] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[ix] += enemyX_change[ix]
        if enemyX[ix] <= 0:
            enemyY[ix] += enemyY_change[ix]
            enemyX_change[ix] = 7
        elif enemyX[ix] >= 736:
            enemyY[ix] += enemyY_change[ix]
            enemyX_change[ix] = -7

        # collision
        collision = is_collision(enemyX[ix], enemyY[ix], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[ix] = random.randint(6, 730)
            enemyY[ix] = random.randint(25, 150)

        enemy(enemyX[ix], enemyY[ix], ix)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
