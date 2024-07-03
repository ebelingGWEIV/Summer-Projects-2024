import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

BG = pygame.transform.scale(pygame.image.load("jediduel.jpg"), (WIDTH, HEIGHT))

BALL_RADIUS = 20


PLAYER_WIDTH = 25
PLAYER_HEIGHT = 150
PLAYER_VEL = 5

divLine_WIDTH = 5
divLine_HEIGHT = HEIGHT

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, playerTwo, divLine, elapsedTime, ball, playerScore, playerTwoScore):
    WIN.blit(BG,(0,0))

    timeText = FONT.render(f"Time: {round(elapsedTime)}s", 1, "Green")
    WIN.blit(timeText, (10, 10))

    pScoreText = FONT.render(f"{playerScore}", 1, "White")
    pTwoScoreText = FONT.render(f"{playerTwoScore}", 1, "White")
    WIN.blit(pScoreText, ((WIDTH / 2) - 35, (10)))
    WIN.blit(pTwoScoreText, ((WIDTH / 2) + 15, 10))

    winGame(playerScore, playerTwoScore)

    pygame.draw.rect(WIN, 'white', player)
    pygame.draw.rect(WIN, 'black', playerTwo)
    pygame.draw.rect(WIN, 'grey', divLine)
    pygame.draw.ellipse(WIN, 'purple', ball)
    pygame.display.update()






def winGame(playerScore, playerTwoScore):
    if playerScore == 3 or playerTwoScore == 3:
        if playerScore == 3:
            winText = FONT.render("Player One wins!", 1, "White")
            WIN.blit(winText, (50, 50))
        else:
            winText = FONT.render("Player Two wins!", 1, "White")
            WIN.blit(winText, (50, 50))

def main():
    run = True

    player = pygame.Rect(15, 350, PLAYER_WIDTH, PLAYER_HEIGHT)
    playerTwo = pygame.Rect(WIDTH - PLAYER_WIDTH - 15, 350, PLAYER_WIDTH, PLAYER_HEIGHT)
    divLine = pygame.Rect((WIDTH / 2) - 5, 0, divLine_WIDTH, divLine_HEIGHT)
    ball = pygame.Rect((WIDTH / 2) - 15, (HEIGHT / 2) - 15, 30, 30)

    ballSpeedX = 5
    ballSpeedY = 5
    incrSpeed = 15000
    speedCount = 0


    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0
    playerScore = 0
    playerTwoScore = 0


    while run:
        speedCount += clock.tick(60)
        elapsedTime = time.time() - startTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and playerTwo.y - PLAYER_VEL >= 0:
            playerTwo.y -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and playerTwo.y + PLAYER_VEL <= HEIGHT - PLAYER_HEIGHT:
            playerTwo.y += PLAYER_VEL

        if keys[pygame.K_a] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_d] and player.y + PLAYER_VEL <= HEIGHT - PLAYER_HEIGHT:
            player.y += PLAYER_VEL

        ball.x += ballSpeedX
        ball.y += ballSpeedY

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ballSpeedY *= -1
        if ball.left <= 0 or ball.right >= WIDTH:
            if ball.left <= 0:
                playerTwoScore += 1
            if ball.right >= WIDTH:
                playerScore += 1
            ballSpeedY = 4
            ballSpeedX = 4
            speedCount = 0
            ball.center = (WIDTH / 2, HEIGHT / 2)
            ballSpeedX *= random.choice((1,-1))
            ballSpeedY *= random.choice((1,-1))
        if ball.colliderect(player) or ball.colliderect(playerTwo):
            ballSpeedX *= -1

        if speedCount >= incrSpeed:
            if ballSpeedX < 0:
                ballSpeedX -= 1
            else:
                ballSpeedX += 1
            if ballSpeedY < 0:
                ballSpeedY -= 1
            else:
                ballSpeedY += 1
            speedCount = 0
















        draw(player, playerTwo, divLine, elapsedTime, ball, playerScore, playerTwoScore)


    pygame.quit()

if __name__ == "__main__":
    main()
